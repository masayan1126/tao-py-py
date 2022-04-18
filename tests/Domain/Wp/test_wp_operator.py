import unittest.mock
import pytest
import requests
import urllib.error

from shared.Domain.Wp.wp_operator import WpOperator


def test_WordPressの記事を取得できる() -> None:

    posts = [
        {
            "id": 1,
            "status": "publish",
            "link": "https://hoge.com",
            "title": "pythonでwordpressの記事を取得する方法",
        },
        {
            "id": 2,
            "status": "publish",
            "link": "https://maasaablog.com/development/python/4506/",
            "title": "pythonで日時オブジェクトを扱う方法",
        },
    ]

    m = unittest.mock.MagicMock()
    m.fetch_posts.return_value = posts

    acutual = m.fetch_posts()
    expected = [
        {
            "id": 1,
            "status": "publish",
            "link": "https://hoge.com",
            "title": "pythonでwordpressの記事を取得する方法",
        },
        {
            "id": 2,
            "status": "publish",
            "link": "https://maasaablog.com/development/python/4506/",
            "title": "pythonで日時オブジェクトを扱う方法",
        },
    ]

    assert acutual == expected


def test_WordPressの記事を取得できる_無効なurlは例外() -> None:
    with pytest.raises(urllib.error.HTTPError):
        wrong_url = "https://hoge.com"

        wp = WpOperator(api_url=wrong_url)
        wp.fetch_posts()


def test_レスポンスヘッダを取得できる() -> None:

    m = unittest.mock.MagicMock()
    m.response_headers.return_value = {
        "Server": "nginx",
        "Content-Type": "application/json; charset=UTF-8",
        "X-WP-Total": "258",
        "X-WP-TotalPages": "26",
    }

    acutual = m.response_headers()
    expected = {
        "Server": "nginx",
        "Content-Type": "application/json; charset=UTF-8",
        "X-WP-Total": "258",
        "X-WP-TotalPages": "26",
    }

    assert acutual == expected


def test_全公開記事数を取得できる() -> None:

    response_headers = {
        "Server": "nginx",
        "Content-Type": "application/json; charset=UTF-8",
        "X-WP-Total": "258",
        "X-WP-TotalPages": "26",
    }

    m = unittest.mock.MagicMock()
    m.total_posts_count.return_value = response_headers["X-WP-Total"]

    acutual = m.total_posts_count()
    expected = "258"

    assert acutual == expected


def test_全ページ数を取得できる() -> None:

    response_headers = {
        "Server": "nginx",
        "Content-Type": "application/json; charset=UTF-8",
        "X-WP-Total": "258",
        "X-WP-TotalPages": "26",
    }

    m = unittest.mock.MagicMock()
    m.total_page_count.return_value = response_headers["X-WP-TotalPages"]

    acutual = m.total_page_count()
    expected = "26"

    assert acutual == expected