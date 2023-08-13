# -- Найти средний балл в группах по определенному предмету.

from sqlalchemy import select, func

from connect_db import session
from models import Faculty, Student, Grade, Subject

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Faculty.name,
                Subject.title,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Faculty)
            .join(Student)
            .join(Grade)
            .join(Subject)
            .filter(Subject.title == "Risk analyst")
            .group_by(Faculty.name, Subject.title)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)
