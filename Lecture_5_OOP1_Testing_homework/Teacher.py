from Lecture_5_OOP1_Testing_homework.Homework import Homework


class Teacher:
    __slots__ = ["last_name", "first_name"]

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, days_count):
        return Homework(text, days_count)
