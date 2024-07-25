import requests
from bs4 import BeautifulSoup

def time_on_website():
    url = 'https://www.findrate.tw/bank/8/'
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
    url = 'https://www.findrate.tw/bank/8/'
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

        # 擷取四個匯率值
        cash_buying_rate = jpy_row[1].get_text(strip=True)
        cash_selling_rate = jpy_row[2].get_text(strip=True)
        spot_buying_rate = jpy_row[3].get_text(strip=True)
        spot_selling_rate = jpy_row[4].get_text(strip=True)

        return {
            'cash_buying_rate': cash_buying_rate,
            'cash_selling_rate': cash_selling_rate,
            'spot_buying_rate': spot_buying_rate,
            'spot_selling_rate': spot_selling_rate
        }

    print("無法獲取匯率資訊")
    return None

def lineNotifyMessage(token, msg):
    headers = {
          "Authorization": "Bearer " + token,
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

rate_date = time_on_website()

rates = get_jpy_exchange_rates()
if rates:
    print(f"日圓現金買入匯率: {rates['cash_buying_rate']}")
    print(f"日圓現金賣出匯率: {rates['cash_selling_rate']}")
    print(f"日圓即期買入匯率: {rates['spot_buying_rate']}")
    print(f"日圓即期賣出匯率: {rates['spot_selling_rate']}")
else:
    print("無法取得日圓匯率") 

token = 'oC2FSw6ud4QTx7fat2jsIbskIxRma4v0XinpQNe7tf5'
message = f"\n更新時間: {rate_date}\n現金買入: {rates['cash_buying_rate']}\n現金賣出: {rates['cash_selling_rate']}\n即期買入: {rates['spot_buying_rate']}\n即期賣出: {rates['spot_selling_rate']}"
# message = f"\n日圓現金買入匯率: {rates['cash_buying_rate']}\n日圓現金賣出匯率: {rates['cash_selling_rate']}\n日圓即期買入匯率: {rates['spot_buying_rate']}\n日圓即期賣出匯率: {rates['spot_selling_rate']}"

lineNotifyMessage(token, message)
token = 'yB7TSamtaWNYEzG8lNPKWhlrgtCEM30rFYWy7n9eecQ'
lineNotifyMessage(token, message)
