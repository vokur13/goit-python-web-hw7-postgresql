# -- Найти студента с наивысшим средним баллом по определенному предмету.

from sqlalchemy import select, func, desc

from connect_db import session
from models import Student, Grade, Subject

if __name__ == "__main__":
    stmt = (
        session.execute(
            select(
                Student.first_name,
                Student.last_name,
                Subject.title,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .select_from(Grade)
            .join(Subject, Grade.subject_id == Subject.id)
            .join(Student, Grade.student_id == Student.id)
            .filter(Subject.title == "Risk analyst")
            .group_by(Student.last_name, Student.first_name, Subject.title)
            .order_by(desc("avg_grade"))
            .limit(1)
        )
        .mappings()
        .all()
    )

    for item in stmt:
        print(item)

# SELECT s.first_name, s.last_name, s1.title, AVG(g.grade)
# FROM students s
# INNER JOIN university.grades g on s.id = g.student_id
# INNER JOIN university.subjects s1 on g.subject_id = s1.id
# WHERE s1.title='Aeronautical engineer'
# GROUP BY  s.last_name, s.first_name, s1.title
# ORDER BY AVG(g.grade) DESC
# LIMIT 5;
