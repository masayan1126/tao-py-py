import pytest
from shared.Enums.ScrapingType import ScrapingType
from shared.Enums.SiteType import SiteType

# 数字で指定すると対応する値(ScrapingType.SELENIUM)が返る
def test_数字からスクレイピング種別を取得できる():
    assert ScrapingType(1) == ScrapingType.SELENIUM


# enumの識別子
def test_スクレイピング種別の識別子を取得できる():
    assert ScrapingType.SOUP.name == "SOUP"


# enumの値
def test_スクレイピング種別の値を取得できる():
    assert ScrapingType.SOUP.value == 2


def test_存在しない種別の場合は例外():
    with pytest.raises(ValueError):
        ScrapingType(99) == ScrapingType.SELENIUM
