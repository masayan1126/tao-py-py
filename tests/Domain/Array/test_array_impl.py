import pytest
from shared.Domain.List.array_impl import ArrayImpl
from shared.Domain.String.xstr import XStr
from shared.array_interface import ArrayInterface


def test_リスト内の全要素を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    acutual = array.all()
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert acutual == expected


def test_リスト内に要素を追加できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    acutual = array.add(11)
    expected = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    assert acutual == expected


def test_リスト内の各要素に処理を適用できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    callback = lambda item: item * 2
    acutual = array.map(callback)
    expected = ArrayImpl([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    assert acutual == expected


def test_リスト内の先頭の要素を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    acutual = array.first()
    expected = 1

    assert acutual == expected


def test_リスト内の先頭の要素を取得できる_要素が存在しない場合は例外() -> None:
    with pytest.raises(IndexError):
        array: ArrayInterface = ArrayImpl([])

        acutual = array.first()


def test_リスト内の要素数を取得できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    acutual = array.count()
    expected = 10

    assert acutual == expected


def test_リストが空かどうかチェックできる() -> None:
    array1: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    array2: ArrayInterface = ArrayImpl([])

    assert array1.is_empty() == False
    assert array2.is_empty() == True


def test_リストをn個に分割したリストを生成できる() -> None:
    array: ArrayInterface = ArrayImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    acutual = array.split(4)
    expected = ArrayImpl([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]])

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
