from datetime import datetime

from Lecture_6_OOP2_homework.homework import Homework


class HomeworkResult:
    __slots__ = ["homework", "solution", "author", "created"]

    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.now()
