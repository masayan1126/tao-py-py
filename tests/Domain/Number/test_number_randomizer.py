import pytest
from shared.Domain.Number.number_randomizer import NumberRandomizer


# @pytest.fixture
# def setuped_list():
#     number_list = [1, 2, 3, 10]
#     return number_list


def test_重複なしのランダムな整数を生成できる():

    i_randomizer = NumberRandomizer()
    numbers = i_randomizer.generate(0, 20, 5)

    actual = len(numbers)
    expected = len(set(numbers))
    assert actual == expected
    assert actual == 5
