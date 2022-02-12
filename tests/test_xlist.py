import pytest

from shared.Util.xlist import XList


@pytest.fixture
def setuped_list():
    number_list = [1, 2, 3, 10]
    return number_list


def test_配列の各要素をmapで2倍にできる(setuped_list):

    multiplication = lambda x: x * 2
    actual = XList.map(multiplication, setuped_list)

    expected = [2, 4, 6, 20]
    assert actual == expected
