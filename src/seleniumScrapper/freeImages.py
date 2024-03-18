from src.seleniumScrapper.config.webdriver import Driver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FreeImages:

    def __init__(self) -> None:
        self.page = 1
        self.itens = []
        self.message = ""
        self.login = "robert.sergio.eng@gmail.com"
        self.password = "JVinxss6bhCkQSL"
        self.url = "https://www.istockphoto.com/"
        self.login_url = "https://www.istockphoto.com/br/sign-in?returnurl=%2Fbr"

        self.driver = Driver().init_driver()

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

    def handle_login(self):
        self.driver.get(self.login_url)
        self.driver.find_element(By.XPATH, '//*[@id="new_session_username"]').send_keys(
            self.login
        )
        self.driver.find_element(By.XPATH, '//*[@id="new_session_password"]').send_keys(
            self.password
        )
        self.driver.find_element(By.XPATH, '//*[@id="sign_in"]').click()

    def handle_logout(self):
        if self.login in self.driver.page_source:
            self.driver.find_element(
                By.XPATH,
                '//*[@id="header-wrapper"]/div/div/header/nav[2]/ul/li[2]/button',
            ).click()
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="header-wrapper"]/div/div/header/nav[2]/ul/nav/div/aside/div[4]/ul/li/a',
                    )
                )
            ).click()
        self.driver.quit()
