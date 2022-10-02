import pytest
from shared.Domain.Scraping.browser_type import BrowserType


def test_数字からブラウザ種別を取得できる() -> None:
    assert BrowserType(1) == BrowserType.CHROME


# enumの識別子
def test_ブラウザ種別の識別子を取得できる() -> None:
    assert BrowserType.FIREFOX.name == "FIREFOX"


# enumの値
def test_ブラウザ種別の値を取得できる() -> None:
    assert BrowserType.CHROME.value == 1


def test_存在しない種別の場合は例外() -> None:
    with pytest.raises(ValueError):
        BrowserType(99)
