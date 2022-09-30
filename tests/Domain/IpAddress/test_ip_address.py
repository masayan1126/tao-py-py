from shared.Domain.IpAddress.ip_address import IpAddress
import pytest


def test_IPアドレスオブジェクトを生成できる() -> None:
    ip = IpAddress("192.0.2.12")

    expected = "192.0.2.12"
    actual = ip.value()

    assert expected == actual


def test_IPアドレスオブジェクトを生成できる_IPアドレスの形式に該当しない場合はエラー() -> None:
    with pytest.raises(ValueError):
        ip = IpAddress("453536646")
        ip.value()
