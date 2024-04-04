import os
import re
import httpx
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from driver import Chrome
from dotenv import load_dotenv
from conf import DOWNDETECTOR_URLS

load_dotenv()

class PaymentChecker(ABC):
    def __init__(self, url):
        self.url = url
    
    @abstractmethod
    def check_accessibility(self) -> dict:
        pass

class HttpPayment(PaymentChecker):
    def check_accessibility(self) -> dict:
        print(self.url)
        return {"eu": httpx.get(self.url).status_code}
    
# -------------------------------------------------------------------

class WebsitePaymentChecker(PaymentChecker):

    def __init__(self):
        self.browser = Chrome(os.environ["CHROMEDRIVER_PATH"])

    def check_accessibility(self) -> dict:
        all_countries_statuses = {}

        print(self.payment_method)
        
        for country, url in self.urls.items():
            html = self.browser.get_html(url)

            if html == None:
                continue

            parsed_response = self._parse_response(html)

            if parsed_response == None:
                continue

            all_countries_statuses[country] = parsed_response

        self.browser.quit()

        return all_countries_statuses
    
# https://downdetector.com/
class DownDetector(WebsitePaymentChecker):
    def __init__(self, payment_method: str):
        super().__init__()
        self.payment_method = payment_method
        self.urls = {country: url.format(payment_method) for country, url in DOWNDETECTOR_URLS.items()}

    def _parse_response(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')

        for script in scripts:
            if 'window.DD.currentServiceProperties' in script.text:
                match = re.search(r"status:\s*'(\w+)'", script.text)
                if match:
                    data = match.group(1)
                    return data
    
# https://www.saashub.com/
class SaasHub(WebsitePaymentChecker):
    def __init__(self, payment_method: str):
        super().__init__()
        self.payment_method = payment_method
        self.urls = {
            "eu": f"https://www.saashub.com/{payment_method}-status"
        }

    def _parse_response(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='level-y gap-4')
        return div.text.replace("\n", "")


jeton = HttpPayment("https://www.jeton.com/payv3/login")
perfectmoney_api = HttpPayment("https://perfectmoney.com/api/")
sticpay = HttpPayment("https://api.sticpay.com/v2/utilities/geoip")
muchbetter = HttpPayment("https://w.api.muchbetter.com/merchant/finish")
pay4fun = HttpPayment("https://p4f.com/")
payid = HttpPayment("https://payid.com.au/")

n26 = SaasHub("n26")
paysafe = SaasHub("paysafe")
qiwi = SaasHub("qiwi")
paysafecard = SaasHub("paysafecard")
perfectmoney = SaasHub("perfectmoney-e-voucher")
neteller = SaasHub("neteller")
skrill = SaasHub("skrill")
bitpay = SaasHub("bitpay")
coinspaid = SaasHub("coinspaid")
visa = DownDetector("visa")
mastercard = DownDetector("mastercard")
apple_pay = DownDetector("apple-pay")
paypal = DownDetector("paypal")
trustly = DownDetector("trustly")
klarna = DownDetector("klarna")
revolut = DownDetector("revolut")
coinbase = DownDetector("coinbase")
binance = DownDetector("binance")

# Формирование строки оповещения
notification_message = ""

# Проверка каждого объекта и формирование оповещения при необходимости
for name, obj in objects.items():
    print(name)
    response = obj.check_accessibility()
    print (obj)
    
    # Обработка объектов типа DownDetector
    if isinstance(obj, DownDetector):
        for country, status in response.items():
            if status == "danger":
                notification_message += f"Платежный сервис {name} недоступен в {country.upper()}\n"
    
    # Обработка объектов типа SaasHub
    elif isinstance(obj, SaasHub):
        if "Down" in response.values():
            notification_message += f"Платежный сервис {name} недоступен\n"
    
    # Обработка ссылочных объектов
    else:
        for country, status_code in response.items():
            expected_code = 200

            if obj.url == "https://api.sticpay.com/v2/utilities/geoip":
                expected_code = 401

            if obj.url == "https://www.jeton.com/payv3/login":
                expected_code = 301

            if status_code != expected_code:
                notification_message += f"Платежный сервис {name} недоступен\n"

# Отправка оповещения, если есть что отправлять
if notification_message:
    send_to_slack(notification_message)