from collections import defaultdict

from Lecture_6_OOP2_homework.homework import Homework
from Lecture_6_OOP2_homework.person import Person


class Teacher(Person):
    homework_done = defaultdict(set)

    def __init__(self, last_name, first_name):
        super().__init__(last_name, first_name)

    @staticmethod
    def create_homework(text, days_count):
        return Homework(text, days_count)

    @staticmethod
    def check_homework(homework_result):
        if len(homework_result.solution) >= 5:
            Teacher.homework_done[homework_result.homework].add(homework_result)
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework=None):
        if isinstance(homework, Homework):
            del Teacher.homework_done[homework]
        else:
            Teacher.homework_done.clear()
