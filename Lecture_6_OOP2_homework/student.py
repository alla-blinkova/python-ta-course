from Lecture_6_OOP2_homework.deadline_error import DeadlineError
from Lecture_6_OOP2_homework.homework_result import HomeworkResult
from Lecture_6_OOP2_homework.person import Person


class Student(Person):
    def __init__(self, last_name, first_name):
        super().__init__(last_name, first_name)

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late")
