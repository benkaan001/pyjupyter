from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

from utils.config import MYSQL_CONFIG

connection_string = f"mysql+mysqlconnector://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}/{MYSQL_CONFIG['database']}"

_engine = create_engine(
    connection_string,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30
)

@contextmanager
def get_db():
    conn = _engine.connect()
    try:
        yield conn
    finally:
        conn.close()

