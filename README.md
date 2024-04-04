# Payment Accessibility Checker

This Python script checks the accessibility of top payment services by sending requests to their respective URLs and parsing the responses. It utilizes Selenium for web scraping and HTTPX for making HTTP requests.

## Installation

1. **Download and install ChromeDriver:**
   - Visit [ChromeDriver download page](https://chromedriver.chromium.org/downloads).
   - Download the latest version of ChromeDriver suitable for your operating system.
   - Unzip the downloaded file and move the `chromedriver` executable to the `/usr/local/bin` directory.

2. **Install Google Chrome:**
   ```bash
   # Add Google Chrome repository
   sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
   sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
   
   # Update system packages
   sudo apt-get -y update
   
   # Install Google Chrome
   sudo apt-get -y install google-chrome-stable
   ```

3. **Set up Python virtual environment:**
   ```bash
   python -m venv venv
   ```

4. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script `payments.py` using the following command:
```bash
python payments.py
```

The script will output the accessibility status of each payment service.

## Supported Payment Services

The script currently supports checking the accessibility of the following payment services:
- Jeton
- Perfect Money API
- Sticpay
- MuchBetter
- Pay4Fun
- PayID
- N26
- Paysafe
- Qiwi
- Paysafecard
- Perfect Money e-Voucher
- Neteller
- Skrill
- Bitpay
- Coinspaid
- Visa
- Mastercard
- Apple Pay
- Paypal
- Trustly
- Klarna
- Revolut
- Coinbase
- Binance

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Disclaimer

This script is provided for educational and informational purposes only. Use it responsibly and at your own risk. The authors of this script are not responsible for any misuse or damage caused by its usage.