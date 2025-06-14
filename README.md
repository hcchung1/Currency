# Currency Tracker

This project provides a Python-based currency tracking tool that monitors exchange rates from Taiwan Bank and Taishin Bank. It can send real-time notifications to your LINE account when specified target exchange rates are achieved.

## Features

*   **Multi-Bank Support:** Fetches and compares exchange rates from multiple Taiwanese banks (currently Taiwan Bank and Taishin Bank).
*   **Currency Tracking:** Allows users to specify a currency to monitor.
*   **Target Rate Notifications:** Users can set target "sell" and "buy" exchange rates.
*   **LINE Integration:** Sends instant notifications via LINE when the monitored currency reaches the specified target rates.
*   **Real-time Monitoring:** Continuously checks exchange rates at regular intervals.
*   **Console Logging:** Prints timestamped updates of the currency checks to the console.

## Configuration

To receive LINE notifications, you need to configure the script with your LINE Notify token.

1.  **Obtain a LINE Notify Token:**
    *   Go to the [LINE Notify website](https://notify-bot.line.me/zh_TW/) and log in with your LINE account.
    *   Navigate to "My Page" or the equivalent section for managing services.
    *   Click on "Generate token" (or similar wording).
    *   Give your token a name (e.g., "CurrencyUpdates") and select the chat or group you want to receive notifications in.
    *   Click "Generate token".
    *   **Important:** Copy the generated token immediately. You will not be able to see it again.

2.  **Configure the Token in the Script:**
    *   The `tracker` function in `Currency_Tracker/Tracker.py` accepts a `token` argument.
    *   When calling this function, pass your LINE Notify token as the `token` parameter.
    *   Example: `tracker(currency="JPY", target=[0.22, 0.21], token="YOUR_LINE_NOTIFY_TOKEN")`

    *Alternatively, you might consider modifying the script to read the token from an environment variable or a configuration file for better security and flexibility, instead of hardcoding it when calling the function.*

## Usage

To use the Currency Tracker, you can call the `tracker` function from `Currency_Tracker.Tracker`.

The `tracker(currency, target, token=None)` function takes the following arguments:

*   `currency` (str): The 3-letter currency code for the currency you want to track (e.g., "JPY", "USD").
*   `target` (list or tuple of floats): A list or tuple containing two float values defining your notification thresholds:
    *   `target_sell_price`: Notify if the bank's currency buying price (your selling price) meets or exceeds this value. (Corresponds to "本行買入" from the banks' perspective).
    *   `target_buy_price`: Notify if the bank's currency selling price (your buying price) meets or falls below this value. (Corresponds to "本行賣出" from the banks' perspective).
*   `token` (str, optional): Your LINE Notify token. If omitted, notifications are printed to the console.

**Example:**

To track the Japanese Yen (JPY) and receive a LINE notification if your selling price for JPY goes at or above 0.22 (Bank Buys JPY from you at >= 0.22), or if your buying price for JPY goes at or below 0.21 (Bank Sells JPY to you at <= 0.21), you would create a Python script or modify `main.py` to call the `tracker` function like this:

```python
from Currency_Tracker.Tracker import tracker

# Your LINE Notify token (optional)
line_token = "YOUR_ACTUAL_LINE_NOTIFY_TOKEN"

# Track JPY: notify if your sell price (bank buys JPY) >= 0.22
# or your buy price (bank sells JPY) <= 0.21
tracker(currency="JPY", target=[0.22, 0.21], token=line_token)
```

You can then execute your script (e.g., `main.py` if you modified it, or your custom script) from your terminal:

```bash
python your_script_name.py
```
*(If you are using `main.py`, you would need to modify it to incorporate this logic, as its current primary function is different.)*

## Prerequisites

*   **Python 3:** Ensure you have Python 3 installed on your system.
*   **Python Libraries:** This project relies on the following Python libraries:
    *   Numpy
    *   Pandas
    *   requests

    You can install these dependencies by running the following command in your terminal, using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Contributing

Contributions to the Currency Tracker are welcome! If you have suggestions for improvements, new features, or find any bugs, please feel free to:

1.  **Open an Issue:** Report bugs or suggest features by opening an issue on the project's GitHub repository.
2.  **Submit a Pull Request:** If you'd like to contribute code:
    *   Fork the repository.
    *   Create a new branch for your feature or bug fix.
    *   Make your changes.
    *   Ensure your code follows the project's style and includes any necessary tests.
    *   Submit a pull request with a clear description of your changes.

We appreciate your help in making this tool better!

## License

This project is licensed under the terms of the MIT License. Please see the [LICENSE](LICENSE) file for more details.
