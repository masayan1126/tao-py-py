from unittest.mock import MagicMock, patch
from shared.Domain.Url.x_url import XUrl
from shared.Domain.Wp.post import Post
from shared.Domain.Wp.wp_operator import WpOperator
from shared.Domain.Wp.wp_operator_impl import WpOperatorImpl
import json


@patch("shared.Domain.Wp.wp_operator_impl.requests")
def test_レスポンスヘッダを取得できる(mock_requests) -> None:
    mock_requests.head.return_value = MagicMock(
        status_code=200,
        headers={
            "Server": "nginx",
            "Content-Type": "application/json; charset=UTF-8",
            "X-WP-Total": "100",
            "X-WP-TotalPages": "10",
        },
    )

    operator: WpOperator = WpOperatorImpl(XUrl("https://hogefoobar.com/"))

    expected = {
        "Server": "nginx",
        "Content-Type": "application/json; charset=UTF-8",
        "X-WP-Total": "100",
        "X-WP-TotalPages": "10",
    }

    assert expected == operator.response_headers()


@patch("shared.Domain.Wp.wp_operator_impl.requests")
def test_全ページ数を取得できる(mock_requests) -> None:

    mock_requests.head.return_value = MagicMock(
        status_code=200,
        headers={
            "Server": "nginx",
            "Content-Type": "application/json; charset=UTF-8",
            "X-WP-Total": "200",
            "X-WP-TotalPages": "20",
        },
    )

    expected = 20
    operator: WpOperator = WpOperatorImpl(XUrl("https://hogefoobar.com/"))

    assert expected == operator.total_page_count()


@patch("shared.Domain.Wp.wp_operator_impl.requests")
def test_全記事数を取得できる(mock_requests) -> None:

    mock_requests.head.return_value = MagicMock(
        status_code=200,
        headers={
            "Server": "nginx",
            "Content-Type": "application/json; charset=UTF-8",
            "X-WP-Total": "150",
            "X-WP-TotalPages": "15",
        },
    )

    expected = 150
    operator: WpOperator = WpOperatorImpl(XUrl("https://hogefoobar.com/"))

    assert expected == operator.total_posts_count()


@patch("shared.Domain.Wp.wp_operator_impl.requests")
def test_WordPressの記事を取得できる_全記事(mock_requests) -> None:

    posts = [
        {
            "id": 1,
            "status": "publish",
            "link": "https://hogefoobar.com",
            "title": {"rendered": "title1"},
        },
        {
            "id": 2,
            "status": "publish",
            "link": "https://hogefoobar.com",
            "title": {"rendered": "title2"},
        },
        {
            "id": 3,
            "status": "publish",
            "link": "https://hogefoobar.com",
            "title": {"rendered": "title3"},
        },
        {
            "id": 4,
            "status": "publish",
            "link": "https://hogefoobar.com",
            "title": {"rendered": "title4"},
        },
    ]

    mock_requests.get.return_value = MagicMock(
        status_code=200, text=f"{json.dumps(posts)}"
    )
    mock_requests.head.return_value = MagicMock(
        status_code=200,
        headers={
            "Server": "nginx",
            "Content-Type": "application/json; charset=UTF-8",
            "X-WP-Total": "4",
            "X-WP-TotalPages": "1",
        },
    )

    operator: WpOperator = WpOperatorImpl(XUrl("https://hogefoobar.com/"))

    expected = [
        Post(
            posts[0]["id"],
            posts[0]["status"],
            posts[0]["link"],
            posts[0]["title"]["rendered"],
        ),
        Post(
            posts[1]["id"],
            posts[1]["status"],
            posts[1]["link"],
            posts[1]["title"]["rendered"],
        ),
        Post(
            posts[2]["id"],
            posts[2]["status"],
            posts[2]["link"],
            posts[2]["title"]["rendered"],
        ),
        Post(
            posts[3]["id"],
            posts[3]["status"],
            posts[3]["link"],
            posts[3]["title"]["rendered"],
        ),
    ]

    assert expected == operator.fetch_posts()
