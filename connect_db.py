import configparser
import pathlib

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

config_path = pathlib.Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(config_path)

USER = config.get("DB_DEV", "USER")
PASSWORD = config.get("DB_DEV", "PASSWORD")
DB_NAME = config.get("DB_DEV", "DB_NAME")
HOST = config.get("DB_DEV", "HOST")
PORT = config.get("DB_DEV", "PORT")

url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(url, echo=True, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()
