import sqlite3

def print_column_names(table_name):
    with sqlite3.connect('../databases/MediaStore.db') as conn:
        cursor = conn.cursor()

        # Get the column names of the specified table
        cursor.execute(f"PRAGMA table_info({table_name})")
        column_names =[col[1] for col in cursor.fetchall()]

        return column_names

