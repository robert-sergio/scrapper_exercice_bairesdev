import pytest
from unittest import mock
from src.beautifulSoupScrapper.freeImages import FreeImages
from mock_response import response_mocks


def test_instance():
    instance = FreeImages()
    assert (
        instance.header.get("User-Agent")
        == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    )


@pytest.fixture
def mock_get_class():
    with mock.patch("requests.get") as mock_get_class:
        yield mock_get_class


def test_response_error(mock_get_class):
    mocked = response_mocks()
    mocked.bad_response()

    mock_get = mock.Mock()
    mock_get.status_code = mocked.status_code
    mock_get.content = mocked.content
    mock_get_class.return_value = mock_get

    instance = FreeImages()
    instance.dogs()
    assert instance.message == "Could not get data: status_code 401"


def test_response_parsing(mock_get_class):
    mocked = response_mocks()
    mocked.good_response()

    mock_get = mock.Mock()
    mock_get.status_code = mocked.status_code
    mock_get.content = mocked.content
    mock_get_class.return_value = mock_get

    instance = FreeImages()
    instance.dogs()
    print(instance.message)
    assert instance.message == "74 dog images captured from website"
