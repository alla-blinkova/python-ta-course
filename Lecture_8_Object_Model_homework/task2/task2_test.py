from Lecture_8_Object_Model_homework.task2.task2 import TableData


def test_len():
    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    assert len(presidents) == 3


def test_contains():
    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    assert ("Yeltsin" in presidents) is True


def test_row():
    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    assert presidents["Yeltsin"] == {"name": "Yeltsin", "age": 999, "country": "Russia"}


def test_iter():
    presidents = TableData(database_name="example.sqlite", table_name="presidents")
    expected_names = ["Yeltsin", "Trump", "Big Man Tyrone"]
    for president in presidents:
        assert president["name"] in expected_names
