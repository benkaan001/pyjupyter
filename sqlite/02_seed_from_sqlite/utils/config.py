import os

HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")
DATABASE = "sqlite_MediaStore"

MYSQL_CONFIG = {
    'user': USER,
    'password': PASSWORD,
    'host': HOST,
    'database': DATABASE,
}

MYSQL_CONFIG_CREATE_DB = {
    'user': USER,
    'password': PASSWORD,
    'host': HOST,
}