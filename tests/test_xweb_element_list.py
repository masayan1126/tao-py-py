import pytest
from shared.Domain.xweb_element_list import XWebElementList


def test_first存在しないキーを指定した場合は例外():
    with pytest.raises(IndexError):
        XWebElementList([]).first()
