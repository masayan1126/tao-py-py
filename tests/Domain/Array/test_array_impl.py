import pytest
from shared.Domain.List.array_impl import ArrayImpl
from shared.Domain.String.xstr import XStr
from shared.array_interface import ArrayInterface


def test_リストをn個に分割したリストを生成できる() -> None:
    array: ArrayInterface = ArrayImpl([1,2,3,4,5,6,7,8,9,10])

    acutual = array.split(4)
    expected = ArrayImpl([
        [1,2,3,4],
        [5,6,7,8],
        [9,10]
    ])

    assert acutual == expected

def test_リスト内の文字列を結合して1つの文字列にできる() -> None:
    array: ArrayInterface = ArrayImpl(["m", "a", "s", "a", "y", "a", "n"])

    acutual = array.to_str()
    expected = XStr("masayan")

    assert acutual == expected


def test_リスト内の文字列を結合して1つの文字列にできる_文字列以外が含まれている場合は例外() -> None:
    with pytest.raises(TypeError):
        array: ArrayInterface = ArrayImpl(["m", 1, "s", False, "y", {}, "n"])

        acutual = array.to_str()


