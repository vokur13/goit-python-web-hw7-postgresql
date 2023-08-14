from sqlalchemy import Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True)
    name = Column(String(56))
    created_at = Column(DateTime, default=func.now())
    students = relationship("Student", backref="faculty")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(56))
    first_name = Column(String(56))
    e_mail = Column(String(128), nullable=False, unique=True)
    faculty_id = Column(Integer, ForeignKey("faculties.id"))
    created_at = Column(DateTime, default=func.now())


class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(56))
    first_name = Column(String(56))
    created_at = Column(DateTime, default=func.now())
    subjects = relationship("Subject", backref="professor")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    title = Column(String(56))
    professor_id = Column(Integer, ForeignKey("professors.id"), nullable=False)
    created_at = Column(DateTime, default=func.now())


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    student = relationship("Student")
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    subject = relationship("Subject")
    grade = Column(Integer)
    date_of = Column(DateTime, nullable=False)
