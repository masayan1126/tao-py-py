import pytest

from shared.Util.dict_util import DictUtil


@pytest.fixture
def setuped():
    return [
        {"id": 1, "name": "taro", "tall": 150},
        {"id": 2, "name": "jiro", "tall": 180},
        {"id": 3, "name": "saburo"},
        {"id": 4, "name": "shiro", "tall": 170},
    ]


def test_特定のキーの値が最も大きい辞書型の要素を返します(setuped):
    d = DictUtil.highest(setuped, "tall", 0)

    expected = d
    actual = setuped[1]

    assert expected == actual
