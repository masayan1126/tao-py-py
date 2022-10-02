from unittest.mock import MagicMock
import pytest
from shared.Core.di_container import DiContainer
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer


def test_id名で要素を取得できること() -> None:
    html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.find_all.return_value = bs4_result_set_mock
    html_analyzer.bind(bs4_mock)
    tag = html_analyzer.find_by_id(id_name="id1")
    assert tag.text == "おすすめの書籍"


def test_id名で要素が見つからない場合は例外() -> None:
    with pytest.raises(IndexError):
        html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
        bs4_mock = MagicMock()
        bs4_mock.find_all.return_value = []
        html_analyzer.bind(bs4_mock)
        tag = html_analyzer.find_by_id(id_name="not exists id")


def test_cssセレクタで要素を取得できること() -> None:
    html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.select.return_value = bs4_result_set_mock
    html_analyzer.bind(bs4_mock)
    result_set = html_analyzer.search_by_selector(selector="selector1")
    assert result_set[0].text == "おすすめの書籍"


def test_class名で要素を取得できること() -> None:
    html_analyzer: HtmlAnalyzer = DiContainer().resolve(HtmlAnalyzer)
    bs4_mock = MagicMock()
    bs4_result_set_mock = MagicMock()
    bs4_tag_mock = MagicMock(text="おすすめの書籍")
    bs4_result_set_mock.__getitem__.return_value = bs4_tag_mock
    bs4_mock.find_all.return_value = bs4_result_set_mock
    html_analyzer.bind(bs4_mock)
    result_set = html_analyzer.search_by_class(class_name="class1")
    assert result_set[0].text == "おすすめの書籍"
