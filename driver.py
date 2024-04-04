from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class Chrome:

    def __init__(self, driver_path: str):
        service = Service(driver_path)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(service=service, options=options)

    def get_html(self, url: str) -> str:

        try:
            self.driver.get(url)

            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'script')))

            html = self.driver.page_source
        except WebDriverException:
            return None

        return html

    def quit(self):
        self.driver.quit()




