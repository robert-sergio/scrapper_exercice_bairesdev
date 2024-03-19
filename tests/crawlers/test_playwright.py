from src.playwright_scrapper.freeImages import FreeImages
from playwright.sync_api import sync_playwright
from unittest.mock import patch
import pathlib


def test_instance():
    instance = FreeImages()
    assert instance.page == None


def test_get_data():
    url = str(pathlib.Path(__file__).parent.resolve()) + "\\mocked_page.html"
    instance = FreeImages()
    with patch.object(instance, "url", new=url):
        with patch.object(instance, "num_page", new=""):
            assert instance.url == url
            assert instance.num_page == ""

            with sync_playwright() as playwright:
                chromium = playwright.chromium
                browser = chromium.launch()
                instance.page = browser.new_page()

                instance.dogs()
                assert instance.message == "73 dog images captured from page "
