"""Init

Revision ID: d4d7b91e34cf
Revises: 
Create Date: 2023-08-12 07:29:30.858515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4d7b91e34cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=56), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=56), nullable=True),
    sa.Column('first_name', sa.String(length=56), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=56), nullable=True),
    sa.Column('first_name', sa.String(length=56), nullable=True),
    sa.Column('e_mail', sa.String(length=128), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculties.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('e_mail')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=56), nullable=True),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('date_of', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('professors')
    op.drop_table('faculties')
    # ### end Alembic commands ###
