from unittest.mock import mock_open, patch
import pytest
from shared.Domain.DataFile.Csv.csv_file_operator_impl import CsvFileOperatorImpl
from shared.Domain.DataFile.data_file_operator_factory import (
    DataFileOperatorFactory,
)
from shared.Domain.DataFile.data_frame_converter import DataFrameConverter
from shared.Domain.FileSystem.file_format_type import FileFormatType
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
import pandas as pd

# id,name,type
# 1,餃子,中華
# 2,明太子パスタ,洋食
# 3,ナスの味噌汁,和食

open_cases_data_provider = [
    (
        "tests/shared/Domain/DataFile/Csv/read_sample1.csv",
        "id,name,type\n1,餃子,中華\n2,明太子パスタ,洋食\n3,ナスの味噌汁,和食",
    ),
    (
        "tests/shared/Domain/DataFile/Csv/read_sample2.csv",
        "id,name,type\n1,餃子,中華\n2,明太子パスタ,洋食\n3,ナスの味噌汁,和食",
    ),
    (
        "tests/shared/Domain/DataFile/Csv/read_sample3.csv",
        "id,name,type\n1,餃子,中華\n2,明太子パスタ,洋食\n3,ナスの味噌汁,和食",
    ),
]
read_cases_data_provider = [
    (
        "tests/shared/Domain/DataFile/Csv/read_sample1.csv",
        [
            {"id": 1, "name": "餃子", "type": "中華"},
            {"id": 2, "name": "明太子パスタ", "type": "洋食"},
            {"id": 3, "name": "ナスの味噌汁", "type": "和食"},
        ],
    ),
    (
        "tests/shared/Domain/DataFile/Csv/read_sample2.csv",
        [
            {"id": 1, "name": "餃子", "type": "中華"},
            {"id": 2, "name": "明太子パスタ", "type": "洋食"},
            {"id": 3, "name": "ナスの味噌汁", "type": "和食"},
        ],
    ),
    (
        "tests/shared/Domain/DataFile/Csv/read_sample3.csv",
        [
            {"id": 1, "name": "餃子", "type": "中華"},
            {"id": 2, "name": "明太子パスタ", "type": "洋食"},
            {"id": 3, "name": "ナスの味噌汁", "type": "和食"},
        ],
    ),
]


@pytest.fixture
def sut() -> CsvFileOperatorImpl:
    csv_file_operator = DataFileOperatorFactory().create(
        file_format_type=FileFormatType.CSV
    )
    return csv_file_operator


@pytest.fixture
def output_filepath() -> XFileSystemPath:
    filepath = XFileSystemPath(
        XStr("tests/shared/Domain/DataFile/Csv/output_sample.csv")
    )
    yield filepath
    filepath.delete()


@pytest.fixture
def output_data() -> list:
    return [
        {
            "id": 1,
            "name": "Python",
            "type": "動的型付け",
        },
        {
            "id": 2,
            "name": "Typescript",
            "type": "静的型付け",
        },
        {
            "id": 3,
            "name": "PHP",
            "type": "動的型付け",
        },
    ]


@pytest.mark.parametrize("filepath, expected", open_cases_data_provider)
def test_open_csvを開くことができる_モック未使用(filepath, expected, sut: CsvFileOperatorImpl):
    actual = sut._open(XFileSystemPath(XStr(filepath))).read()
    assert expected == actual


def test_open_csvを開くことができる_モック使用(sut: CsvFileOperatorImpl):
    file_name: str = "no_exists.txt"
    result = "id,name,type1,餃子,中華2,明太子パスタ,洋食3,ナスの味噌汁,和食".encode()
    open_mock = mock_open(read_data=result)

    with patch("builtins.open", open_mock):
        expected = "id,name,type1,餃子,中華2,明太子パスタ,洋食3,ナスの味噌汁,和食"
        actual = sut._open(XFileSystemPath(XStr(file_name))).read()
        assert expected == actual


@pytest.mark.parametrize("filepath, expected", read_cases_data_provider)
def test_read_csvを読み取ることができる_モック未使用(filepath, expected, sut: CsvFileOperatorImpl):
    actual = sut.read(XFileSystemPath(XStr(filepath)))
    assert expected == actual


def test_read_csvを読み取ることができる_モック使用(sut: CsvFileOperatorImpl):
    file_name: str = "no_exists.txt"
    result = "id,name,type1,餃子,中華2,明太子パスタ,洋食3,ナスの味噌汁,和食".encode()
    open_mock = mock_open(read_data=result)

    df = pd.DataFrame(
        data={
            "id": ["1", "2", "3"],
            "name": ["餃子", "明太子パスタ", "ナスの味噌汁"],
            "type": ["中華", "洋食", "和食"],
        }
    )

    with patch("builtins.open", open_mock):
        with patch(
            "shared.Domain.DataFile.Csv.csv_file_operator_impl.read_table",
            return_value=df,
        ):
            expected = DataFrameConverter.to_list(df)
            actual = sut.read(XFileSystemPath(XStr(file_name)))
            assert expected == actual


def test_output_csvを出力することができる_モック未使用(
    sut: CsvFileOperatorImpl, output_filepath: XFileSystemPath, output_data: list
):

    sut.output(
        output_filepath,
        data_list=output_data,
    )

    expected = output_data
    actual = sut.read(output_filepath)
    assert expected == actual


@patch("shared.Domain.DataFile.Csv.csv_file_operator_impl.DataFrame")
def test_output_csvを出力することができる_モック使用(
    data_frame_mock,
    sut: CsvFileOperatorImpl,
    output_filepath: XFileSystemPath,
    output_data: list,
):

    data_frame_mock.return_value = pd.DataFrame(output_data)

    sut.output(
        output_filepath,
        data_list=output_data,
    )

    expected = output_data
    actual = sut.read(output_filepath)
    assert expected == actual
