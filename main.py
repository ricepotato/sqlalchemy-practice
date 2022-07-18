import os

from config import AppConfig
from models import Address, User


def remove_if_exists(path: str):
    if os.path.exists(path):
        os.remove(path)


def main():
    # db 파일 있으면 삭제함
    sqlite_db_filepath = "db.sqlite"
    remove_if_exists(sqlite_db_filepath)

    app_config = AppConfig()
    repository = app_config.get_sqlite_repository()

    addr = Address(name="home", address="seoul")
    new_user = User(
        name="ricepotato",
        email="sukjun40@naver.com",
        addresses=[
            addr,
        ],
    )

    new_user_id = repository.add(new_user)

    user = repository.get_user(new_user_id)
    print(user.name)
    repository.delete_user_by_id(user.id)


if __name__ == "__main__":
    main()
