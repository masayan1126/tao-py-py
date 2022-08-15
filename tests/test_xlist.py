import pytest

from shared.Domain.xlist import XList


@pytest.fixture
def setuped_list():
    number_list = [1, 2, 3, 10]
    return number_list


def test_配列の各要素をmapで2倍にできる(setuped_list):

    actual = XList.map(lambda x: x * 2, setuped_list)

    expected = [2, 4, 6, 20]
    assert actual == expected
