from bs4 import BeautifulSoup
import pytest
import requests
from shared.Domain.xbeautiful_soup import XBeautifulSoup
from shared.Application.find_web_element_service import FindWebElementService


@pytest.fixture
def setuped_xbeautiful_soup():
    base_path = "https://maasaablog.com/"
    res = requests.get(base_path)
    return XBeautifulSoup(BeautifulSoup(res.text, "html.parser"))


def test_対象のページからhtml要素を取得できること(setuped_xbeautiful_soup: XBeautifulSoup):
    title_tag_list = FindWebElementService(
        setuped_xbeautiful_soup
    ).find_element_by_tag_name("title")
    assert title_tag_list[0].text == "masayanblog | 現役のweb系エンジニアが役立つ情報をまったりご紹介"
