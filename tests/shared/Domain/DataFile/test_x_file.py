import pytest
from shared.Domain.DataFile.x_file import XFile
from shared.Domain.Url.x_url import XUrl


@pytest.fixture(scope="module")  # module(テストファイル全体で1回実行)
def sut() -> XFile:
    return XFile(
        x_url=XUrl(
            encoded_href="https://3.bp.blogspot.com/-X6ruoCYjbMQ/WSa8zi2McUI/AAAAAAABEhc/OtxhrQP4PYIusK-uT61_NHbxUmlEbLWgACLcB/s800/cat_mikeneko2.png"
        )
    )


def test_ファイルオブジェクトからファイルのurlを取得できる(sut: XFile):
    assert (
        sut.filepath().href()
        == "https://3.bp.blogspot.com/-X6ruoCYjbMQ/WSa8zi2McUI/AAAAAAABEhc/OtxhrQP4PYIusK-uT61_NHbxUmlEbLWgACLcB/s800/cat_mikeneko2.png"
    )


def test_ファイルオブジェクトからファイル名のみを取得できる(sut: XFile):
    assert sut.filename() == "cat_mikeneko2.png"


def test_ファイルオブジェクトから拡張子を取得できる(sut: XFile):
    assert sut.extension() == ".png"
