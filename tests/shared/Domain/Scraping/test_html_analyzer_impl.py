from unittest.mock import MagicMock, patch
import pytest
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.Scraping.html_analyzer_factory import HtmlAnalyzerFactory
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
@patch("shared.Domain.Scraping.html_analyzer_factory.requests")
def sut(mock_requests):
    mock_requests.get.return_value = MagicMock(status_code=200, content="dummy binary")
    return HtmlAnalyzerFactory().create(XUrl("https://maasaablog.com"))


def test_id名で要素を取得できる(sut: HtmlAnalyzer) -> None:
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.find_all.return_value = bs4_result_set_mock
    sut.bind(bs4_mock)
    tag = sut.find_by_id(id_name="id1")
    assert tag.text == "おすすめの書籍"


def test_id名で要素が見つからない場合は例外(sut: HtmlAnalyzer) -> None:
    with pytest.raises(IndexError):
        bs4_mock = MagicMock()
        bs4_mock.find_all.return_value = []
        sut.bind(bs4_mock)
        tag = sut.find_by_id(id_name="not exists id")


def test_cssセレクタで要素を取得できる(sut: HtmlAnalyzer) -> None:
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.select.return_value = bs4_result_set_mock
    sut.bind(bs4_mock)
    result_set = sut.search_by_selector(selector="selector1")
    assert result_set[0].text == "おすすめの書籍"


def test_class名で要素を取得できる(sut: HtmlAnalyzer) -> None:
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.find_all.return_value = bs4_result_set_mock
    sut.bind(bs4_mock)
    result_set = sut.search_by_class(class_name="class1")
    assert result_set[0].text == "おすすめの書籍"
