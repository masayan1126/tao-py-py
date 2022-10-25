from unittest.mock import patch
import pytest
from shared.Domain.DataFile.data_file_operator_factory import (
    DataFileOperatorFactory,
)
from shared.Domain.DataFile.data_frame_converter import DataFrameConverter
from shared.Domain.DataFile.Excel.excel_file_operator_impl import ExcelFileOperatorImpl
from shared.Domain.FileSystem.file_format_type import FileFormatType
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr
import pandas as pd


read_cases_data_provider = [
    (
        "tests/shared/Domain/DataFile/Excel/read_sample1.xlsx",
        [
            {
                "プログラミング言語一覧": [
                    {"id": 1, "name": "PHP", "type": "動的型付け"},
                    {"id": 2, "name": "Java", "type": "静的型付け"},
                    {"id": 3, "name": "Python", "type": "動的型付け"},
                    {"id": 4, "name": "Ruby", "type": "動的型付け"},
                ]
            },
            {
                "フレームワーク一覧": [
                    {"id": 1, "name": "Laravel"},
                    {"id": 2, "name": "Sprint"},
                    {"id": 3, "name": "Django"},
                    {"id": 4, "name": "RonR"},
                ]
            },
        ],
    ),
    (
        "tests/shared/Domain/DataFile/Excel/read_sample2.xlsx",
        [
            {
                "出荷一覧": [
                    {
                        "shipping_id": 1,
                        "shipping_date": pd.Timestamp("2022-10-01 00:00:00"),
                        "delivery_date": pd.Timestamp("2022-10-02 00:00:00"),
                    },
                    {
                        "shipping_id": 2,
                        "shipping_date": pd.Timestamp("2022-10-02 00:00:00"),
                        "delivery_date": pd.Timestamp("2022-10-03 00:00:00"),
                    },
                    {
                        "shipping_id": 3,
                        "shipping_date": pd.Timestamp("2022-10-03 00:00:00"),
                        "delivery_date": pd.Timestamp("2022-10-04 00:00:00"),
                    },
                    {
                        "shipping_id": 4,
                        "shipping_date": pd.Timestamp("2022-10-04 00:00:00"),
                        "delivery_date": pd.Timestamp("2022-10-05 00:00:00"),
                    },
                ]
            },
            {
                "請求一覧": [
                    {
                        "billing_id": 1,
                        "date": pd.Timestamp("2022-10-01 00:00:00"),
                        "billing_amount": 2000,
                    },
                    {
                        "billing_id": 2,
                        "date": pd.Timestamp("2022-10-02 00:00:00"),
                        "billing_amount": 3000,
                    },
                    {
                        "billing_id": 3,
                        "date": pd.Timestamp("2022-10-03 00:00:00"),
                        "billing_amount": 2000,
                    },
                    {
                        "billing_id": 4,
                        "date": pd.Timestamp("2022-10-04 00:00:00"),
                        "billing_amount": 3000,
                    },
                ]
            },
        ],
    ),
]


@pytest.fixture
def sut() -> ExcelFileOperatorImpl:
    excel_file_operator = DataFileOperatorFactory().create(
        file_format_type=FileFormatType.EXCEL
    )
    return excel_file_operator


@pytest.fixture
def output_filepath() -> XFileSystemPath:
    filepath = XFileSystemPath(
        XStr("tests/shared/Domain/DataFile/Excel/output_sample1.xlsx")
    )
    yield filepath
    # filepath.delete()


@pytest.fixture
def output_data_list() -> list:
    return [
        {
            "プログラミング言語一覧": [
                {"id": 1, "name": "PHP", "type": "動的型付け"},
                {"id": 2, "name": "Java", "type": "静的型付け"},
                {"id": 3, "name": "Python", "type": "動的型付け"},
                {"id": 4, "name": "Ruby", "type": "動的型付け"},
            ]
        },
        {
            "フレームワーク一覧": [
                {"id": 1, "name": "Laravel"},
                {"id": 2, "name": "Sprint"},
                {"id": 3, "name": "Django"},
                {"id": 4, "name": "RonR"},
            ]
        },
    ]


@pytest.mark.parametrize("filepath, expected", read_cases_data_provider)
def test_read_excelを読み取ることができる_モック未使用(filepath, expected, sut: ExcelFileOperatorImpl):
    actual = sut.read(XFileSystemPath(XStr(filepath)))
    assert expected == actual


def test_read_excelを読み取ることができる_モック使用(sut: ExcelFileOperatorImpl):

    excel_workbook_data = {
        "プログラミング言語一覧": pd.DataFrame(
            [
                {"id": 1, "name": "PHP", "type": "動的型付け"},
                {"id": 2, "name": "Java", "type": "静的型付け"},
                {"id": 3, "name": "Python", "type": "動的型付け"},
                {"id": 4, "name": "Ruby", "type": "動的型付け"},
            ]
        ),
        "フレームワーク一覧": pd.DataFrame(
            [
                {"id": 1, "name": "Laravel"},
                {"id": 2, "name": "Sprint"},
                {"id": 3, "name": "Django"},
                {"id": 4, "name": "RonR"},
            ]
        ),
    }

    with patch(
        "shared.Domain.DataFile.Excel.excel_file_operator_impl.read_excel",
        return_value=excel_workbook_data,
    ):
        expected = [
            {sheetname: DataFrameConverter.to_list(dataframe)}
            for sheetname, dataframe in excel_workbook_data.items()
        ]
        actual = sut.read(XFileSystemPath(XStr("not_exists_excel_path")))
        assert expected == actual


def test_output_excelを出力することができる_モック未使用(
    sut: ExcelFileOperatorImpl, output_filepath: XFileSystemPath, output_data_list: list
):

    for dictionary in output_data_list:
        for sheet_name, data_list in dictionary.items():
            sut.output(
                filepath=output_filepath,
                sheet_name=sheet_name,
                data_list=data_list,
            )

    expected = output_data_list
    actual = sut.read(output_filepath)
    assert expected == actual


@patch("shared.Domain.DataFile.Excel.excel_file_operator_impl.DataFrame")
def test_output_excelを出力することができる_モック使用(
    data_frame_mock,
    sut: ExcelFileOperatorImpl,
    output_filepath: XFileSystemPath,
    output_data_list: list,
):

    data_frame_mock.return_value = [
        pd.DataFrame(output_data_list[0]["プログラミング言語一覧"]),
        pd.DataFrame(output_data_list[1]["フレームワーク一覧"]),
    ]

    for dictionary in output_data_list:
        for sheet_name, data_list in dictionary.items():
            sut.output(
                filepath=output_filepath,
                sheet_name=sheet_name,
                data_list=data_list,
            )

    expected = output_data_list
    actual = sut.read(output_filepath)
    assert expected == actual
