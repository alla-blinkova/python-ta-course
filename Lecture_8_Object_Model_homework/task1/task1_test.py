import pytest

from Lecture_8_Object_Model_homework.task1.task1 import KeyValueStorage


def test_item():
    storage = KeyValueStorage("task1.txt")
    assert storage["name"] == "kek"


def test_attribute():
    storage = KeyValueStorage("task1.txt")
    assert storage.song == "shadilay"


def test_int():
    storage = KeyValueStorage("task1.txt")
    assert storage.power == 9001


def test_wrong_key():
    with pytest.raises(ValueError):
        KeyValueStorage("task1_broken.txt")


def test_built_in():
    storage = KeyValueStorage("task1.txt")
    assert storage.__class__ is KeyValueStorage
