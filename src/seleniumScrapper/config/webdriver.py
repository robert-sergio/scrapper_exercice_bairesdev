from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self) -> None:
        self.strategy = ""
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("log-level=3")
        self.options.add_argument("--headless")

    def init_driver(self):
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=self.options
        )
