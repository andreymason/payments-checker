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

print(jeton.check_accessibility())
print("")
print(perfectmoney_api.check_accessibility())
print("")
print(sticpay.check_accessibility())
print("")
print(muchbetter.check_accessibility())
print("")
print(pay4fun.check_accessibility())
print("")


payid = SaasHub("payid")
n26 = SaasHub("n26")
paysafe = SaasHub("paysafe")
qiwi = SaasHub("qiwi")
paysafecard = SaasHub("paysafecard")
perfectmoney = SaasHub("perfectmoney-e-voucher")
neteller = SaasHub("neteller")
skrill = SaasHub("skrill")
bitpay = SaasHub("bitpay")
coinspaid = SaasHub("coinspaid")

print(payid.check_accessibility())
print("")
print(n26.check_accessibility())
print("")
print(paysafe.check_accessibility())
print("")
print(qiwi.check_accessibility())
print("")
print(paysafecard.check_accessibility())
print("")
print(perfectmoney.check_accessibility())
print("")
print(neteller.check_accessibility())
print("")
print(skrill.check_accessibility())
print("")
print(bitpay.check_accessibility())
print("")
print(coinspaid.check_accessibility())
print("")

visa = DownDetector("visa")
mastercard = DownDetector("mastercard")
apple_pay = DownDetector("apple-pay")
paypal = DownDetector("paypal")
trustly = DownDetector("trustly")
klarna = DownDetector("klarna")
revolut = DownDetector("revolut")
coinbase = DownDetector("coinbase")
binance = DownDetector("binance")

print(visa.check_accessibility())
print("")
print(mastercard.check_accessibility())
print("")
print(apple_pay.check_accessibility())
print("")
print(paypal.check_accessibility())
print("")
print(trustly.check_accessibility())
print("")
print(klarna.check_accessibility())
print("")
print(revolut.check_accessibility())
print("")
print(coinbase.check_accessibility())
print("")
print(binance.check_accessibility())

