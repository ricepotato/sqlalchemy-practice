# sqlalchemy

## session

## commit

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
