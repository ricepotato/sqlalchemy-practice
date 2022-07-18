from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

from repository import SqlalchemyRepository


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class AppConfig(Singleton):
    def __init__(self):
        self._sqlite_session = None
        self._mysql_session = None

    def get_sqlite_repository(self):
        return SqlalchemyRepository(self.sqlite_session)

    def get_mysql_repository(self):
        return SqlalchemyRepository(self.mysql_session)

    @property
    def sqlite_session(self):
        """sqlite session 객체 생성/반환
        하나의 sqlite session 만 유지한다"""

        if self._sqlite_session:
            return self._sqlite_session

        sqlite_db_filepath = "db.sqlite"
        engine = create_engine(f"sqlite:///{sqlite_db_filepath}")
        Base.metadata.create_all(bind=engine)
        Sess = sessionmaker(bind=engine, autocommit=False)
        self._sqlite_session = Sess()
        return self._sqlite_session

    @property
    def mysql_session(self):
        pass
