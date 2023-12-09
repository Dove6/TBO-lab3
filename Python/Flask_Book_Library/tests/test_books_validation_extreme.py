import pytest
from typing import Literal, Optional
from project.books.models import Book

str_extreme_values = [
    "A" * 1000,
    "A" * 10000,
    "A" * (2**16),  # 1 over max length of MySQL VARCHAR
    "A" * (2**32),  # 1 over max length of SQL Server VARCHAR
]

str_extreme_value_ids = [
    '"A" * 1000',
    '"A" * 10000',
    '"A" * (2**16)',
    '"A" * (2**32)',
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
    str_extreme_values,
    ids=str_extreme_value_ids,
)
def test_invalid_name(invalid_name: str):
    with pytest.raises(Exception):
        _create_book(name=invalid_name)


@pytest.mark.parametrize(
    "invalid_author",
    str_extreme_values,
    ids=str_extreme_value_ids,
)
def test_invalid_author(invalid_author: str):
    with pytest.raises(Exception):
        _create_book(author=invalid_author)


@pytest.mark.parametrize(
    "invalid_year_published",
    [
        10000,
        100000,
        1000000,
        2**15,  # 1 over i16
        2**16,  # 1 over u16
        2**31,  # 1 over i32
        2**32,  # 1 over u32
        -10000,
        -100000,
        -1000000,
    ],
)
def test_invalid_year_published(invalid_year_published: int):
    with pytest.raises(Exception):
        _create_book(year_published=invalid_year_published)


@pytest.mark.parametrize(
    "invalid_book_type",
    str_extreme_values,
    ids=str_extreme_value_ids,
)
def test_invalid_book_type(invalid_book_type: str):
    with pytest.raises(Exception):
        _create_book(book_type=invalid_book_type)


@pytest.mark.parametrize(
    "invalid_status",
    str_extreme_values,
    ids=str_extreme_value_ids,
)
def test_invalid_status(invalid_status: str):
    with pytest.raises(Exception):
        _create_book(status=invalid_status)
