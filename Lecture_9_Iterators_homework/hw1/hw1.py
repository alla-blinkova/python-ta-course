"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
# [1, 2, 3, 4, 5, 6]

Add tests for this function.
"""
from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    output_list = []
    for filepath in file_list:
        with open(filepath, mode="r") as input_file:
            numbers = [int(line) for line in input_file]
            output_list.extend(numbers)
    return iter(sorted(output_list))
