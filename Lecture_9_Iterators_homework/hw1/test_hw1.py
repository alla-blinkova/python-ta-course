import pytest

from Lecture_9_Iterators_homework.hw1.hw1 import merge_sorted_files


@pytest.mark.parametrize(
    "files,expected_result",
    [
        (["file1.txt"], [1, 3, 5]),
        (["file1.txt", "file2.txt"], [1, 2, 3, 4, 5, 6]),
        (["file1.txt", "file2.txt", "file3.txt"], [-1, 1, 2, 2, 3, 4, 5, 6, 7]),
    ],
)
def test_positive(files, expected_result):
    assert list(merge_sorted_files(files)) == expected_result


def test_wrong_format():
    with pytest.raises(ValueError):
        list(merge_sorted_files(["file1.txt", "broken_file.txt"]))
