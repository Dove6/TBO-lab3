from datetime import datetime
import pytest
from typing import Literal, Optional
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
    "correct_name",
    [
        "Do Androids Dream of Electric Sheep?",
        "The Lion, the Witch and the Wardrobe",
        "I Can Read With My Eyes Shut!",
        "Fahrenheit 451",
    ],
)
def test_correct_name(correct_name: str):
    _create_book(name=correct_name)


@pytest.mark.parametrize(
    "correct_name",
    [
        "I",
        "A" * 64,
    ],
)
def test_correct_name_length_edge_cases(correct_name: str):
    _create_book(name=correct_name)


@pytest.mark.parametrize(
    "correct_author",
    [
        "Philip K. Dick",
        "C. S. Lewis",
        "Dr. Seuss",
        "Ray Bradbury",
    ],
)
def test_correct_author(correct_author: str):
    _create_book(author=correct_author)


@pytest.mark.parametrize(
    "correct_author",
    [
        "V",
        "C" * 64,
    ],
)
def test_correct_author_length_edge_cases(correct_author: str):
    _create_book(author=correct_author)


@pytest.mark.parametrize(
    "correct_year_published",
    [
        1900,
        1950,
        2000,
    ],
)
def test_correct_year_published(correct_year_published: int):
    _create_book(year_published=correct_year_published)


@pytest.mark.parametrize(
    "correct_year_published",
    [
        -600,
        -1,
        0,
        1,
        datetime.utcnow().year,
    ],
)
def test_correct_year_published_value_edge_cases(correct_year_published: int):
    _create_book(year_published=correct_year_published)


@pytest.mark.parametrize(
    "correct_book_type",
    [
        "2days",
        "5days",
        "10days",
    ],
)
def test_correct_book_type(correct_book_type: Literal["2days", "5days", "10days"]):
    _create_book(book_type=correct_book_type)


@pytest.mark.parametrize(
    "correct_status",
    [
        "available",
    ],
)
def test_correct_status(correct_status: Literal["available"]):
    _create_book(status=correct_status)
