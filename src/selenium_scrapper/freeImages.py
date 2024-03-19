from src.selenium_scrapper.config.webdriver import Driver
from selenium.webdriver.common.by import By
from datetime import datetime
from src.logger.logger import logger


class FreeImages:

    def __init__(self) -> None:
        self.num_page = 1
        self.itens = []
        self.message = ""
        self.login = "dummyEmail@email.com"
        self.password = "JVinxss6bhCkQSL"
        self.url = "https://www.freeimages.com/"
        self.login_url = "https://www.freeimages.com/signin"
        self.mapped_banners = ["Check our Plans", "iStock"]

        self.driver = Driver().init_driver()

    def dogs(self):
        num_page = self.num_page
        url = f"{self.url}{num_page}"
        self.driver.get(url)
        divs = self.driver.find_elements(
            By.XPATH,
            '//*[@id="content-wrapper"]/div[3]/div[2]/div[2]/div',
        )

        for div in divs:

            alt = div.find_element(By.TAG_NAME, "img").get_attribute("alt")
            src = div.find_element(By.TAG_NAME, "img").get_attribute("src")

            if alt in self.mapped_banners:
                continue
            data = {
                "page": url,
                "url": src,
                "alt": alt,
                "date_happened": datetime.now(),
            }
            self.itens.append(data)
        self.message = f"{len(divs)} dog images captured from page {num_page}"
        logger.info(f"{len(divs)} dog images captured from page {num_page}")

    def handle_login(self):
        self.driver.get(self.login_url)
        self.driver.find_element(By.XPATH, '//*[@id="username-input"]').send_keys(
            self.login
        )
        self.driver.find_element(By.XPATH, '//*[@id="password-input"]').send_keys(
            self.password
        )
        self.driver.find_element(By.XPATH, '//*[@id="btn-signin-submit"]').click()
        logger.info("Ran Website Login Example")
