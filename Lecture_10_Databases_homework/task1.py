from sqlalchemy import create_engine, MetaData

from Lecture_10_Databases_homework.model import Base

engine = create_engine("sqlite:///main.db")
connection = engine.connect()
metadata = MetaData()
Base.metadata.create_all(engine)
