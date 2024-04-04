# Payment Accessibility Checker

This Python script checks the accessibility of top payment services by sending requests to their respective URLs and parsing the responses. It utilizes Selenium for web scraping and HTTPX for making HTTP requests.

## Basis of Checks

The accessibility checks in this script are based on HTTP requests to the respective URLs of payment services. The script sends requests to DownDetector and SaasHub websites to retrieve information about the status of these services. Based on the responses received, it determines whether the payment services are accessible or not.

The script utilizes the following sources for checking accessibility:
- **DownDetector**: Provides real-time status updates and reports for various services, including payment platforms.
- **SaasHub**: Aggregates information about software-as-a-service (SaaS) products, including payment services, and provides status updates.

These sources are queried to gather data about the availability of payment services across different regions. The script then processes this information to determine whether each service is accessible or not.

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

## Environment Configuration

Before running the script, you need to set up a `.env` file to store environment variables, such as `CHROMEDRIVER_PATH`, which specifies the path to the ChromeDriver executable.

Create a `.env` file in the root directory of the project and add the following line:
```plaintext
CHROMEDRIVER_PATH=/path/to/chromedriver
```
Replace `/path/to/chromedriver` with the actual path to your ChromeDriver executable.

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