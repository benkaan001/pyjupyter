import sqlite3

def get_all_employees():
    """
    Fetches all employees data from the SQLite database and returns it as a list of tuples

    Returns:
    list: A list of tuples representing employee data
    """
    with sqlite3.connect('./data/employee_data.db') as sqlite_conn:
        cursor = sqlite_conn.cursor()
        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()
    return data