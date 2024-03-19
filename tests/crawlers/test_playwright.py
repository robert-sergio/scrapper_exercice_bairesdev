from src.playwright_scrapper.freeImages import FreeImages
from playwright.sync_api import sync_playwright


def test_instance():
    instance = FreeImages()
    assert instance.page == None


def test_get_data():
    instance = FreeImages()
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch()
        instance.page = browser.new_page()
        instance.dogs()

    assert instance.page.url == "https://www.freeimages.com/search/dogs/1"
    assert instance.message == "73 dog images captured from page 1"
