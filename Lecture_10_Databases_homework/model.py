import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    student = relationship("Student")
    teacher = relationship("Teacher")


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    homework_result = relationship("HomeworkResult")


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    homework = relationship("Homework")


class Homework(Base):
    __tablename__ = "homework"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    deadline = Column(DateTime)
    teacher = Column(Integer, ForeignKey("teacher.id"))
    homework_result = relationship("HomeworkResult")


class HomeworkResult(Base):
    __tablename__ = "homework_result"
    id = Column(Integer, primary_key=True)
    homework = Column(Integer, ForeignKey("homework.id"))
    solution = Column(String)
    author = Column(Integer, ForeignKey("student.id"))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    homework_done = relationship("HomeworkDone")


class HomeworkDone(Base):
    __tablename__ = "homework_done"
    id = Column(Integer, primary_key=True)
    homework_result_id = Column(Integer, ForeignKey("homework_result.id"))
