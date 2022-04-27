import pytest
from shared.Domain.File.x_file import XFile
from shared.Domain.Url.x_url import XUrl


@pytest.fixture
def setuped_xfile() -> XFile:
    return XFile(
        x_url=XUrl(
            encoded_href="https://3.bp.blogspot.com/-X6ruoCYjbMQ/WSa8zi2McUI/AAAAAAABEhc/OtxhrQP4PYIusK-uT61_NHbxUmlEbLWgACLcB/s800/cat_mikeneko2.png"
        )
    )


def test_ファイルオブジェクトからファイル名のみを取得できること(setuped_xfile: XFile):

    assert setuped_xfile.filename() == "cat_mikeneko2.png"


def test_ファイルオブジェクトから拡張子を取得できること(setuped_xfile: XFile):

    assert setuped_xfile.extension() == ".png"
