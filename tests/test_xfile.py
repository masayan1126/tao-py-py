from shared.Domain.xfile import XFile
from shared.Domain.xurl import XUrl

from logging import INFO, ERROR, getLogger

logger = getLogger("test")


def test_ファイルオブジェクトから拡張子を取得できること():

    x_file = XFile(
        x_url=XUrl(
            href="https://www.meti.go.jp/press/2021/06/20210616004/20210616004-1.pdf"
        )
    )

    assert x_file.get_extension() == ".pdf"


def test_ファイルオブジェクトからファイル名のみを取得できること():

    x_file = XFile(
        x_url=XUrl(
            href="https://www.meti.go.jp/press/2021/06/20210616004/20210616004-1.pdf"
        )
    )

    logger.debug("debug", x_file.get_file_name())

    assert x_file.get_file_name() == "20210616004-1.pdf"
