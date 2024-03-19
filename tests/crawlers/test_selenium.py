from src.selenium_scrapper.freeImages import FreeImages


def test_instance():
    instance = FreeImages()
    assert instance.driver.name == "chrome-headless-shell"


def test_get_data():
    instance = FreeImages()
    instance.dogs()
    assert instance.driver.current_url == "https://www.freeimages.com/search/dogs/1"
    assert instance.message == "74 dog images captured from page 1"
