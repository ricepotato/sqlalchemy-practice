# sqlalchemy

## session


`Session` 은 스스로 만들거나 `sessionmaker` class 를 사용해서 만들어진다. 일반적으로 앞으로 연결될 하나의 `Engine` 을 전달받는다. 일반적으로 아래 코드와 같이 사용한다.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# an Engine, which the Session will use for connection
# resources
engine = create_engine('postgresql://scott:tiger@localhost/')

# create session and add objects
with Session(engine) as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()
```

위 코드에서, `Session` 객체는 특정한 database URL 과 연결된 `Engine` 를 사용해서 만들어진다. Python context manager 를 사용해서 만들어지는데, block 끝에서 자동으로 `session` 을 닫는다. 이것은 `Session.close()` method 를 호출하는 것과 동일하다.


`Session.commit()` 를 호출하는 것은 선택적이다. 이것은 `Session` 이 데이터를 database 에 추가하는 작업 있는 경우에만 필요하다. SELECT query 는 데이터를 쓰지 않기 때문에 `Session.commit()` 을 호출하는 작업이 불필요하다.

#### Note
`Session.commit()` 이 호출되고난 이후, 명시적이든 context manager 를 사용하든 만료된 `Session` 과 연관되어있는 모든 객체들은 다음 transaction 에서 다시 로드하기 위해 전부 삭제된다. 다른 `Session` 과 연관되기 전까지 객체를 사용할 수 없다. `Session.expire_on_commit` parameter 를 사용하면 이러한 동작을 비활성화 할 수 있다.


### commit


## flush

모든 변경사항을 database 로 내보냅니다.

Writes out all pending object creations, deletions and modifications
to the database as INSERTs, DELETEs, UPDATEs, etc. Operations are
automatically ordered by the Session's unit of work dependency
solver.

Database operations will be issued in the current transactional
context and do not affect the state of the transaction, unless an
error occurs, in which case the entire transaction is rolled back.
You may flush() as often as you like within a transaction to move
changes from Python to the database's transaction buffer.

For `autocommit` Sessions with no active manual transaction, flush()
will create a transaction on the fly that surrounds the entire set of
operations into the flush.

## autocommit

기본값 false

autocommit=True 상태에서는 session.begin() 을 명시적으로 호출해야 transaction 이 시작된다.

## autoflush
