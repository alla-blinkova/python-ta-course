"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from typing import Callable, Iterable
import re


def validate_line(line: str) -> bool:
    return len(line.split()) == 5


def validate_date(date: str) -> bool:
    regexp = re.compile(r'.*\d{4}-\d{2}-\d{2}$')
    return bool(regexp.match(date))


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    filepath_out = "results.txt"
    with open(filepath, mode="r") as file_input, open(filepath_out, mode="w") as file_output:
        for line in file_input:
            for validator in validators:
                is_valid = validator(line.rstrip())
                if not is_valid:
                    file_output.write("{} {}\n".format(line.rstrip(), validator.__name__))
                    break
    return filepath_out
