import pytest
from shared.Domain.List.array_impl import ArrayImpl
from shared.Domain.String.xstr import XStr
from shared.array_interface import ArrayInterface


def test_リスト内の全要素を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    actual = array.all()
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert expected == actual


def test_リスト内に要素を追加できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    actual = array.add(11)
    expected = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    assert expected == actual


def test_リスト内の各要素に処理を適用できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    callback = lambda item: item * 2
    actual = array.map(callback)
    expected = ArrayImpl([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    assert expected == actual


def test_リスト内の先頭の要素を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    actual = array.first()
    expected = 1

    assert expected == actual


def test_リスト内の先頭の要素を取得できる_要素が存在しない場合は例外() -> None:
    with pytest.raises(IndexError):
        array: ArrayInterface = ArrayImpl([])

        actual = array.first()


def test_リスト内の要素数を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    actual = array.count()
    expected = 10

    assert expected == actual


def test_条件に一致するリスト内の要素数を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    callback = lambda val: val <= 5

    actual = array.count(callback)
    expected = 5

    assert expected == actual


def test_リストが空かどうかチェックできる() -> None:
    array1: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    array2: ArrayInterface = ArrayImpl([])

    assert array1.is_empty() == False
    assert array2.is_empty() == True


def test_リストをn個に分割したリストを生成できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    actual = array.split(4)
    expected = ArrayImpl([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]])

    assert expected == actual


def test_リスト内の文字列を結合して1つの文字列にできる() -> None:
    array: ArrayInterface = ArrayImpl(["m", "a", "s", "a", "y", "a", "n"])

    actual = array.to_str()
    expected = XStr("masayan")

    assert expected == actual


def test_リスト内の文字列を結合して1つの文字列にできる_文字列以外が含まれている場合は例外() -> None:
    with pytest.raises(TypeError):
        array: ArrayInterface = ArrayImpl(["m", 1, "s", False, "y", {}, "n"])

        actual = array.to_str()
