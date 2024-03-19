from src.selenium_scrapper.freeImages import FreeImages
import pathlib
from unittest.mock import patch


def test_instance():
    instance = FreeImages()
    assert instance.driver.name == "chrome-headless-shell"


def test_get_data():
    url = str(pathlib.Path(__file__).parent.resolve()) + "\\mocked_page.html"
    instance = FreeImages()
    with patch.object(instance, "url", new=url):
        with patch.object(instance, "num_page", new=""):
            assert instance.url == url
            assert instance.num_page == ""

            instance.dogs()

            assert instance.message == "74 dog images captured from page "
