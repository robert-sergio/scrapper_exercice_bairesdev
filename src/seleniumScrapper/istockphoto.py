from seleniumScrapper.config.webdriver import Driver
from selenium.webdriver.common.by import By
from datetime import datetime


class IstockPhoto:

    def __init__(self) -> None:
        self.page = 1
        self.itens = []
        self.message = ""
        self.driver = Driver().init_driver()

    def retry(self): ...

    def dogs(self):
        url = f"https://www.istockphoto.com/br/search/2/image?mediatype=photography&phrase=dog&page={self.page}"
        self.driver.get(url)
        divs = self.driver.find_elements(
            By.XPATH,
            "/html/body/div[2]/section/div/main/div/div/div[2]/div/div[3]/div",
        )

        for div in divs:
            src = div.find_element(By.TAG_NAME, "img").get_attribute("src")
            alt = div.find_element(By.TAG_NAME, "img").get_attribute("alt")
            data = {
                "page": url,
                "url": src,
                "alt": alt,
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
