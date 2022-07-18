from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import ForeignKey

import models

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("email", String(50)),
)

address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE")),
    Column("name", String(50)),
    Column("address", String(200)),
)


def start_mappers():
    address_mapper = mapper(models.Address, address)
    _ = mapper(
        models.User,
        user,
        properties={"addresses": relationship(address_mapper, collection_class=list)},
    )
