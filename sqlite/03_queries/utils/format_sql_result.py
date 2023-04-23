from tabulate import tabulate

def format_sql_result(query_result):
    """
    Format the results of a SQL query stored in a Python variable as a text table using the tabulate library.

    Parameters:
    query_result (ResultSet): A ResultSet object containing the results of a SQL query.

    Returns:
    None: The function prints the formatted table to the console using the `print` function.

    Example Usage:
        >>> format_sql_result(query_result)
        | Country   |   AvgRevenuePerCustomer |   TotalRevenue |
        |-----------|------------------------|----------------|
        | Germany   |                 1.39714|         156.48 |
        | France    |                 1.11486|         195.09 |
        | Brazil    |                 1.08629|         190.09 |
        | Canada    |                 0.67848|         303.95 |
        | USA       |                 0.44214|         523.06 |
    """

    header = query_result.keys
    rows = [row for row in query_result]
    return  print(tabulate(rows, headers=header, tablefmt='pipe'))