from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql+psycopg2://postgres:password@localhost:5432/university"
)
Session = sessionmaker(bind=engine)
session = Session()
