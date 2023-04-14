import mysql.connector
from mysql.connector import errorcode
from IPython.core.magic import register_line_magic
from IPython import get_ipython
from config import MYSQL_CONFIG
from sqlalchemy import create_engine

@register_line_magic
def connect_to_mysql(line):
    try:
        with mysql.connector.connect(**MYSQL_CONFIG) as conn:
            print("Connection established.")
            return conn
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username and password.")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(e)

# Set the SQL connection string using the MYSQL_CONFIG info
sql_conn_str = f'mysql+mysqlconnector://{MYSQL_CONFIG["user"]}:{MYSQL_CONFIG["password"]}@{MYSQL_CONFIG["host"]}/{MYSQL_CONFIG["database"]}'

# Set the SQLalchemy engine
engine = create_engine(sql_conn_str)

# Set up the %sql magic command
def load_ipython_extension(ipython):
    ipython.register_magic_function(connect_to_mysql, magic_kind='line')

# Automatically load the extension when the module is imported
load_ipython_extension(get_ipython())