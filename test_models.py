from faker import Faker
from models import User, Address


def test_user_create():
    faker = Faker()
    user = User(name="sukjun.sagong", email="ricepotato40@gmail.com")
    assert user

    addr = Address(name="home", address=faker.address())
    assert addr
