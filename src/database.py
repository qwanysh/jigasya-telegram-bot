from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src import config

engine = create_engine(url=config.DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
