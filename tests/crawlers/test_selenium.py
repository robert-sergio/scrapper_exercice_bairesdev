from src.selenium_scrapper.freeImages import FreeImages
import pathlib
from unittest.mock import patch
import os


def test_instance():
    instance = FreeImages()
    assert instance.driver.name == "chrome-headless-shell"


def test_get_data():
    if os.name == "posix":
        url = (
            "file://"
            + str(pathlib.Path(__file__).parent.resolve())
            + "/mocked_page.html"
        )
    else:
        url = str(pathlib.Path(__file__).parent.resolve()) + "\\mocked_page.html"
    instance = FreeImages()
    with patch.object(instance, "url", new=url):
        with patch.object(instance, "num_page", new=""):
            assert instance.url == url
            assert instance.num_page == ""

            instance.retrieve_images()

            assert instance.message == "74 images captured from page "
