import sys, os

cur_path = os.path.dirname(os.path.abspath(__file__))
head, tail = os.path.split(os.path.split(cur_path)[0])
sys.path.insert(0, os.path.join(head, 'src'))
sys.path.insert(1, os.path.join(head, 'tests'))



import pytest
from src.person import Person, Email, PersonDAO


@pytest.fixture
def valid_person():
    return Person(1, "John Doe", 30)


@pytest.fixture
def invalid_person():
    return Person(2, "Jane", 300)


@pytest.fixture
def valid_email():
    return Email(1, "john@example.com")


@pytest.fixture
def invalid_email():
    return Email(2, "invalid_email")


def test_save_valid_person(valid_person, valid_email):
    valid_person.emails.append(valid_email)
    dao = PersonDAO()
    dao.save(valid_person)
    assert len(dao.persons) == 1


def test_save_invalid_person(invalid_person):
    dao = PersonDAO()
    dao.save(invalid_person)
    assert len(dao.persons) == 0


def test_is_name_valid():
    dao = PersonDAO()
    assert dao.is_name_valid("John Doe") is True
    assert dao.is_name_valid("Jane") is False
    assert dao.is_name_valid("123 John") is False


def test_is_age_valid():
    dao = PersonDAO()
    assert dao.is_age_valid(30) is True
    assert dao.is_age_valid(300) is False


def test_person_has_email():
    dao = PersonDAO()
    valid_email = Email(1, "john@example.com")
    assert dao.person_has_email([valid_email]) is True
    assert dao.person_has_email([]) is False


def test_is_email_valid():
    dao = PersonDAO()
    assert dao.is_email_valid("john@example.com") is True
    assert dao.is_email_valid("invalid_email") is False
