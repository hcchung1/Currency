import os
import requests
from bs4 import BeautifulSoup

def time_on_website():
    url = 'https://www.findrate.tw/bank/25/'
    response = requests.get(url)
    response.encoding = 'utf-8'  # 確保編碼正確
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # find the class named "Unit"
        rate_date_tag = soup.find('a', id='rate_date')
        if rate_date_tag:
            rate_date = rate_date_tag.get_text(strip=True)
            print(f"匯率更新日期時間: {rate_date}")
            return rate_date
        else:
            print("找不到匯率更新日期時間")

def get_jpy_exchange_rates():
    url = 'https://www.findrate.tw/bank/25/'
    response = requests.get(url)
    response.encoding = 'utf-8'  # 確保編碼正確
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到日圓的表格行
        jpy_row = None
        table = soup.find('table')
        if not table:
            print("找不到匯率表格")
            return None

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if cells and '日幣 JPY' in cells[0].get_text(strip=True):
                jpy_row = cells
                break

        if not jpy_row:
            print("找不到日圓匯率行")
            return None

        # 擷取即期匯率
        spot_buying_rate = jpy_row[3].get_text(strip=True)
        spot_selling_rate = jpy_row[4].get_text(strip=True)

        return {
            'spot_buying_rate': spot_buying_rate,
            'spot_selling_rate': spot_selling_rate
        }

    print("無法獲取匯率資訊")
    return None

def telegram_send_message(token, chat_id, msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg
    }
    r = requests.post(url, data=payload)
    return r.status_code

rate_date = time_on_website()

rates = get_jpy_exchange_rates()
if rates:
    print(f"日圓即期買入匯率: {rates['spot_buying_rate']}")
    print(f"日圓即期賣出匯率: {rates['spot_selling_rate']}")
else:
    print("無法取得日圓匯率") 

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

if rates and bot_token and chat_id:
    message = (
        f"\n更新時間: {rate_date}"
        f"\n即期買入: {rates['spot_buying_rate']}"
        f"\n即期賣出: {rates['spot_selling_rate']}"
    )
    telegram_send_message(bot_token, chat_id, message)
else:
    print("無法送出 Telegram 訊息，請檢查匯率或環境變數")
