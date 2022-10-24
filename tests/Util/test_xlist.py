import pytest
from shared.Domain.xlist import XList


@pytest.fixture
def setuped():
    number_list = [1, 2, 3, 10]
    return number_list


def test_配列の各要素の数値を2倍にできる(setuped):

    expected = [2, 4, 6, 20]
    actual = XList.map(lambda x: x * 2, setuped)

    assert expected == actual
