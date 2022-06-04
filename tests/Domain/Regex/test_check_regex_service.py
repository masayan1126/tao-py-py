from shared.Domain.Regex.xregex import XRegex
from shared.Domain.Regex.check_regex_service import CheckRegexService
from shared.Domain.String.xstr import XStr
import re


def test_正規表現に一致する文字列を返すこと():

    # テーラードジャケット 対象商品（性別：メンズ）古着｜テーラードジャケット（メンズ）
    xstr = XStr(
        "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/?p_gtype=2"
    )
    xregex = XRegex(".+?(?=\?)")

    assert (
        CheckRegexService().check(xregex, xstr=xstr)
        == "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/"
    )


def test_正規表現に一致する文字列を返すこと_match():

    # テーラードジャケット 対象商品（性別：メンズ）古着｜テーラードジャケット（メンズ）
    xstr = XStr(
        "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/?p_gtype=2"
    )
    xregex = XRegex(".+?(?=\?)")
    matches = re.match(xregex.pattern(), xstr.value())

    assert (
        matches.group()
        == "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/"
    )

def test_正規表現に一致する文字列を返すこと_IPv4():


    xstr = XStr(
        "192.168.0.2"
    )
    xregex = XRegex('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    
    assert (
        CheckRegexService().check(xregex, xstr=xstr)
        == "192.168.0.2"
    )


def test_正規表現に一致する文字列を返すこと_search():

    # テーラードジャケット 対象商品（性別：メンズ）古着｜テーラードジャケット（メンズ）
    xstr = XStr(
        "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/?p_gtype=2"
    )
    xregex = XRegex(".+?(?=\?)")
    matches = re.search(xregex.pattern(), xstr.value())

    assert (
        matches.group()
        == "https://zozo.jp/men-category/jacket-outerwear/tailored-jacket/"
    )


def test_正規表現に一致する文字列がない場合は引数の文字列をそのまま返すこと():

    xstr = XStr("hogemaru")
    xregex = XRegex(".+?(?=\?)")

    assert CheckRegexService().check(xregex, xstr=xstr) == "hogemaru"
