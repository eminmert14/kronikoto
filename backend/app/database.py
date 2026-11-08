from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

logger = logging.getLogger("kronikoto")

db_url = settings.database_url
connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {"connect_timeout": 2}

try:
    engine = create_engine(db_url, connect_args=connect_args)
    if not db_url.startswith("sqlite"):
        with engine.connect() as conn:
            pass
except Exception as e:
    print(f"UYARI: {db_url} baglantisi kurulamadi ({e}). Gecici olarak SQLite (kronikoto.db) kullaniliyor.")
    db_url = "sqlite:///./kronikoto.db"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
