import pytest
from typing import Literal, Optional
from project.books.models import Book

# source: https://github.com/payloadbox/sql-injection-payload-list (chosen 16 lines)
SQLi_list = [
    "'='",
    "'LIKE'",
    "' OR 'x'='x",
    "' AND id IS NULL; --",
    "'''''''''''''UNION SELECT '2",
    "%00",
    "+",
    "||",
    "%",
    "1 AND (SELECT * FROM Users) = 1",
    "or 1=1",
    "or 1=1--",
    "or 1=1#",
    "or 1=1/*",
    "admin' --",
    "admin' or '1'='1",
]

# source: https://github.com/payloadbox/xss-payload-list (first 16 lines)
XSS_list = [
    '"-prompt(8)-"',
    "'-prompt(8)-'",
    '";a=prompt,a()//',
    "';a=prompt,a()//",
    "'-eval(\"window['pro'%2B'mpt'](8)\")-'",
    "\"-eval(\"window['pro'%2B'mpt'](8)\")-\"",
    '"onclick=prompt(8)>"@x.y',
    '"onclick=prompt(8)><svg/onload=prompt(8)>"@x.y',
    "<image/src/onerror=prompt(8)>",
    "<img/src/onerror=prompt(8)>",
    "<image src/onerror=prompt(8)>",
    "<img src/onerror=prompt(8)>",
    "<image src =q onerror=prompt(8)>",
    "<img src =q onerror=prompt(8)>",
    "</scrip</script>t><img src =q onerror=prompt(8)>",
    "'`\"><\x3Cscript>javascript:alert(1)</script>",
]


def _create_book(
    name: Optional[str] = None,
    author: Optional[str] = None,
    year_published: Optional[int] = None,
    book_type: Optional[Literal["2days", "5days", "10days"]] = None,
    status="available",
) -> Book:
    # Dummy values (valid but meaningless)
    if name is None:
        name = "name"
    if author is None:
        author = "author"
    if year_published is None:
        year_published = 2000
    if book_type is None:
        book_type = "2days"
    Book(name, author, year_published, book_type, status)


@pytest.mark.parametrize(
    "invalid_name",
    SQLi_list,
)
def test_invalid_name_SQLi(invalid_name: str):
    with pytest.raises(Exception):
        _create_book(name=invalid_name)


@pytest.mark.parametrize(
    "invalid_name",
    XSS_list,
)
def test_invalid_name_XSS(invalid_name: str):
    with pytest.raises(Exception):
        _create_book(name=invalid_name)


@pytest.mark.parametrize(
    "invalid_author",
    SQLi_list,
)
def test_invalid_author_SQLi(invalid_author: str):
    with pytest.raises(Exception):
        _create_book(author=invalid_author)


@pytest.mark.parametrize(
    "invalid_author",
    XSS_list,
)
def test_invalid_author_XSS(invalid_author: str):
    with pytest.raises(Exception):
        _create_book(author=invalid_author)


@pytest.mark.parametrize(
    "invalid_year_published",
    SQLi_list,
)
def test_invalid_year_published_SQLi(invalid_year_published: str):
    with pytest.raises(Exception):
        _create_book(year_published=invalid_year_published)


@pytest.mark.parametrize(
    "invalid_year_published",
    XSS_list,
)
def test_invalid_year_published_XSS(invalid_year_published: str):
    with pytest.raises(Exception):
        _create_book(year_published=invalid_year_published)


@pytest.mark.parametrize(
    "invalid_book_type",
    SQLi_list,
)
def test_invalid_book_type_SQLi(invalid_book_type: str):
    with pytest.raises(Exception):
        _create_book(book_type=invalid_book_type)


@pytest.mark.parametrize(
    "invalid_book_type",
    XSS_list,
)
def test_invalid_book_type_XSS(invalid_book_type: str):
    with pytest.raises(Exception):
        _create_book(book_type=invalid_book_type)


@pytest.mark.parametrize(
    "invalid_status",
    SQLi_list,
)
def test_invalid_status_SQLi(invalid_status: str):
    with pytest.raises(Exception):
        _create_book(status=invalid_status)


@pytest.mark.parametrize(
    "invalid_status",
    XSS_list,
)
def test_invalid_status_XSS(invalid_status: str):
    with pytest.raises(Exception):
        _create_book(status=invalid_status)
