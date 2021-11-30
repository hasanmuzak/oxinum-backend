from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import Models

SQLALCHEMY_DATABASE_URL = "sqlite:///./oxinum.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}

)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
