import sqlite3

def get_sqlite_schema(table_name: str = "employees") -> list:
    """
    Get the schema information for a SQLite table, defaults to 'employees' table

    Args:
        table_name: The name of the table to get the schema for

    Returns:
        A list of tuples, where each tuple contains the following values for a column:
        (id, name, type, notnull, default_value, primary_key)
    """
    with sqlite3.connect('./data/employee_data.db') as conn:
        cursor = conn.cursor()
        metadata_query = f"""PRAGMA table_info({table_name})"""
        cursor.execute(metadata_query)
        schema = cursor.fetchall()
        return schema