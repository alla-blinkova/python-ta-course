"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
#
# For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
# 6
# >>> universal_file_counter(test_dir, "txt", str.split)
# 6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    file_paths = [
        f"{dir_path}\\{file}"
        for file in os.listdir(dir_path)
        if file.endswith(file_extension)
    ]
    count = 0
    for path in file_paths:
        with open(path, mode="r") as input_file:
            if tokenizer:
                file_content = input_file.read()
                count = count + len(tokenizer(file_content))
            else:
                count = count + len(input_file.readlines())
    return count
