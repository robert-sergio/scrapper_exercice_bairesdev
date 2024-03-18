from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self) -> None:
        self.strategy = ""
        self.options = Options()
        # self.options.page_load_strategy = "none"
        # self.options.add_argument("--headless")

    def init_driver(self):
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=self.options
        )
