import pytest
from shared.Domain.Scraping.html_analyzer import HtmlAnalyzer
from shared.Domain.Scraping.html_analyzer_factory import (
    HtmlAnalyzerFactory,
)
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def setuped_html_analyzer() -> None:
    return HtmlAnalyzerFactory().create(XUrl("https://maasaablog.com"))


def test_id名で要素が見つからない場合は例外(setuped_html_analyzer: HtmlAnalyzer) -> None:
    with pytest.raises(IndexError):
        setuped_html_analyzer.find_by_id(id_name="nothing_id")


def test_id名で要素を取得できること(setuped_html_analyzer: HtmlAnalyzer) -> None:
    tag = setuped_html_analyzer.find_by_id(id_name="custom_html-4")
    assert tag.h3.text == "おすすめの書籍"


def test_cssセレクタで要素が見つからない場合は例外(setuped_html_analyzer: HtmlAnalyzer) -> None:
    with pytest.raises(IndexError):
        setuped_html_analyzer.find_by_selector(selector=".c > b > #c")


def test_cssセレクタで要素を取得できること(setuped_html_analyzer: HtmlAnalyzer) -> None:
    tag = setuped_html_analyzer.find_by_selector(selector=".logo > a > span")
    assert tag.text == "masayanblog"


def test_class名で要素を取得できること(setuped_html_analyzer: HtmlAnalyzer) -> None:
    result_set = setuped_html_analyzer.search_by_class(class_name="logo")
    assert result_set[0].a.text == "masayanblog"


def test_class名で要素が見つからない場合は空配列(setuped_html_analyzer: HtmlAnalyzer) -> None:
    result_set = setuped_html_analyzer.search_by_class(class_name="nothing_class")
    assert len(result_set) == 0
