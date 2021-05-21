import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Lecture_10_Databases_homework.model import (
    Person,
    Student,
    Teacher,
    Homework,
    HomeworkResult,
    HomeworkDone,
)

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(id=1, last_name="Ivanov", first_name="Ivan")
person2 = Person(id=2, last_name="Petrov", first_name="Alexander")

student = Student(id=1, person_id=1)

teacher = Teacher(id=1, person_id=2)

homework = Homework(
    id=1,
    text="OOP homework",
    deadline=datetime.datetime.utcnow() + datetime.timedelta(days=5),
    teacher=1,
)

homework_result = HomeworkResult(
    id=1, homework=1, solution="OOP homework solution", author=1
)

session.add_all([person1, person2, student, teacher, homework, homework_result])
session.commit()

homework_done_1 = HomeworkDone(id=1, homework_result_id=1)

session.add(homework_done_1)
session.commit()
session.close()
