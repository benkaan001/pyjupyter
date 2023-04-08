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