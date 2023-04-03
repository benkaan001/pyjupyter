import sqlite3

def get_mysql_data_type(sqlite_type: str) -> str:
    """
    Get the equivalent MySQL data type for a given SQLite data type

    Args:
        sqlite_type: The SQLite data type to convert

    Returns:
        The equivalent MySQL data type
    """
    data_type_map = {"integer": "INT",
                     "real": "FLOAT",
                     "text": "VARCHAR(255)",
                     "blob": "BLOB",
                     }
    return data_type_map.get(sqlite_type.lower(), "VARCHAR(255)")


def get_sqlite_schema(table_name: str = "employees") -> list:
    """
    Get the schema information for a SQLite table, defaults to 'employees' table

    Args:
        table_name: The name of the table to get the schema for

    Returns:
        A list of tuples, where each tuple contains the following values for a column:
        (id, name, type, notnull, default_value, primary_key)
    """
    with sqlite3.connect('employee_database.db') as conn:
        cursor = conn.cursor()
        metadata_query = f"""PRAGMA table_info({table_name})"""
        cursor.execute(metadata_query)
        schema = cursor.fetchall()
        return schema