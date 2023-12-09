from datetime import datetime
import pytest
from typing import Any, Literal, Optional
from project.books.models import Book


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
    [
        "\n\r\t\b\f\v\a",
        "\x00\x01\x02\x03\x04\x05\x06\x07",
        "####################",
        "         ",
        "!@#$%^&*()_+{}|:\"<>?-=[]\;',./\\",
    ],
)
def test_invalid_name(invalid_name: str):
    with pytest.raises(Exception):
        _create_book(name=invalid_name)


@pytest.mark.parametrize(
    "name_with_bad_type",
    [
        None,
        1234,
        3.1416,
        (),
        [],
        {},
        lambda x: x,
    ],
)
def test_invalid_name_with_bad_type(name_with_bad_type: Any):
    with pytest.raises(Exception):
        _create_book(name=name_with_bad_type)


@pytest.mark.parametrize(
    "invalid_name",
    [
        "",
        "A" * 65,
    ],
)
def test_invalid_name_length_edge_cases(invalid_name: str):
    with pytest.raises(Exception):
        _create_book(name=invalid_name)


@pytest.mark.parametrize(
    "invalid_author",
    [
        "\n\r\t\b\f\v\a",
        "\x00\x01\x02\x03\x04\x05\x06\x07",
        "####################",
        "         ",
        "!@#$%^&*()_+{}|:\"<>?-=[]\;',./\\",
    ],
)
def test_invalid_author(invalid_author: str):
    with pytest.raises(Exception):
        _create_book(author=invalid_author)


@pytest.mark.parametrize(
    "author_with_bad_type",
    [
        None,
        1234,
        3.1416,
        (),
        [],
        {},
        lambda x: x,
    ],
)
def test_invalid_author_with_bad_type(author_with_bad_type: Any):
    with pytest.raises(Exception):
        _create_book(author=author_with_bad_type)


@pytest.mark.parametrize(
    "invalid_author",
    [
        "",
        "B" * 65,
    ],
)
def test_invalid_author_length_edge_cases(invalid_author: str):
    with pytest.raises(Exception):
        _create_book(author=invalid_author)


@pytest.mark.parametrize(
    "invalid_year_published",
    [
        2500,
        3000,
        -300000,
    ],
)
def test_invalid_year_published(invalid_year_published: int):
    with pytest.raises(Exception):
        _create_book(year_published=invalid_year_published)


@pytest.mark.parametrize(
    "invalid_year_published",
    [
        # The year when the first book ever was written is not known for sure
        datetime.utcnow().year + 1,
    ],
)
def test_invalid_year_published_value_edge_cases(invalid_year_published: int):
    with pytest.raises(Exception):
        _create_book(year_published=invalid_year_published)


@pytest.mark.parametrize(
    "year_published_with_bad_type",
    [
        None,
        "abcdef",
        3.1416,
        (),
        [],
        {},
        lambda x: x,
    ],
)
def test_invalid_year_published_with_bad_type(year_published_with_bad_type: Any):
    with pytest.raises(Exception):
        _create_book(year_published=year_published_with_bad_type)


@pytest.mark.parametrize(
    "invalid_book_type",
    [
        "",
        "a",
        "100days",
        "1day",
    ],
)
def test_invalid_book_type(invalid_book_type: str):
    with pytest.raises(Exception):
        _create_book(book_type=invalid_book_type)


@pytest.mark.parametrize(
    "book_type_with_bad_type",
    [
        None,
        1234,
        3.1416,
        (),
        [],
        {},
        lambda x: x,
    ],
)
def test_invalid_book_type_with_bad_type(book_type_with_bad_type: Any):
    with pytest.raises(Exception):
        _create_book(book_type=book_type_with_bad_type)


@pytest.mark.parametrize(
    "invalid_status",
    [
        "",
        "a",
        "unavailable",
    ],
)
def test_invalid_status(invalid_status: str):
    with pytest.raises(Exception):
        _create_book(status=invalid_status)


@pytest.mark.parametrize(
    "status_with_bad_type",
    [
        None,
        1234,
        3.1416,
        (),
        [],
        {},
        lambda x: x,
    ],
)
def test_invalid_status_with_bad_type(status_with_bad_type: Any):
    with pytest.raises(Exception):
        _create_book(status=status_with_bad_type)
