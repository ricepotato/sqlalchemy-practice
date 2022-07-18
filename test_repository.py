from typing import List
from faker import Faker
from repository import SqlalchemyRepository
from models import User, Address


def test_sqlalchemy_repository_can_add_user(autocommit_sqlite_session):
    repo = SqlalchemyRepository(session=autocommit_sqlite_session)
    user = User(name="sukjun.sagong", email="ricepotato40@gmail.com")

    id = repo.add(user)
    assert id

    user1 = repo.get_user(id)
    assert user1.name == user.name

    user.name = "sukjun.sagong2"
    id_updated = repo.add(user)
    assert id_updated == id

    user2 = repo.get_user(id)
    assert user2.name == user.name


def test_sqlalchemy_repository_all_users(autocommit_sqlite_session, fake_users):
    repo = SqlalchemyRepository(session=autocommit_sqlite_session)
    assert all(map(lambda user: repo.add(user), fake_users))
    users = repo.get_users()
    assert users


def test_sqlalchemy_repository_can_add_address(autocommit_sqlite_session):
    repo = SqlalchemyRepository(session=autocommit_sqlite_session)
    faker = Faker()
    address = Address(name=faker.word(), address=faker.address())
    id = repo.add(address)
    assert id


def test_sqlalchemy_repository_add_user_address(
    autocommit_sqlite_session, fake_addresses
):
    repo = SqlalchemyRepository(session=autocommit_sqlite_session)
    user = User(name="sukjun.sagong", email="ricepotato40@gmail.com")
    user.addresses = fake_addresses
    user_id = repo.add(user)
    new_user = repo.get_user(user_id)
    addresses = repo.get_addresses_by_user(new_user)
    assert addresses


def test_sqlalchemy_repository_delete_user(
    autocommit_sqlite_session, fake_users: List[User]
):
    repo = SqlalchemyRepository(session=autocommit_sqlite_session)
    assert all(map(lambda user: repo.add(user), fake_users))
    users = repo.get_users()
    assert len(users) == 10

    assert repo.delete_user(users[3])

    users = repo.get_users()
    assert len(users) == 9
