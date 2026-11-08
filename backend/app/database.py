from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

import os
from pathlib import Path

logger = logging.getLogger("kronikoto")

BASE_DIR = Path(__file__).resolve().parent.parent
default_sqlite_path = BASE_DIR / "kronikoto.db"

db_url = settings.database_url
if db_url.startswith("sqlite") and not os.path.exists(db_url.replace("sqlite:///", "")):
    if default_sqlite_path.exists():
        db_url = f"sqlite:///{default_sqlite_path.as_posix()}"

connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {"connect_timeout": 2}

try:
    engine = create_engine(db_url, connect_args=connect_args)
    if not db_url.startswith("sqlite"):
        with engine.connect() as conn:
            pass
except Exception as e:
    print(f"UYARI: {db_url} baglantisi kurulamadi ({e}). Gecici olarak SQLite (kronikoto.db) kullaniliyor.")
    db_url = f"sqlite:///{default_sqlite_path.as_posix()}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
