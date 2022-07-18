import os
import pytest
from faker import Faker
from models import User, Address

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base


def remove_if_exists(path: str):
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def sqlite_db():
    sqlite_db_filepath = "db.sqlite"
    remove_if_exists(sqlite_db_filepath)
    engine = create_engine(f"sqlite:///{sqlite_db_filepath}")
    Base.metadata.create_all(bind=engine)

    yield engine

    remove_if_exists(sqlite_db_filepath)


@pytest.fixture
def autocommit_sqlite_session(sqlite_db):
    Sess = sessionmaker(bind=sqlite_db, autocommit=True)
    session: Session = Sess()
    yield session
    session.close()


@pytest.fixture
def fake_users():
    faker = Faker()
    return [User(name=faker.name(), email=faker.email()) for _ in range(10)]


@pytest.fixture
def fake_addresses():
    faker = Faker()
    return [Address(name=faker.word(), address=faker.address()) for _ in range(2)]
