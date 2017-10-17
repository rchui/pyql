""" datalib.py

This file defines functions that deal with data handling.
"""

import sys
from pathlib import Path

def load(database):
    """ Gets the list of tables in the database.

    Args:
        database: the name of the database.

    Returns:
        tables: the tables of the database.
    """
    with open(database) as db_file:
        tables = []
        for line in db_file:
            table = line.strip()
            if Path(table).is_file(): # If the table exists.
                tables.append(table)
            else: # Else exit.
                sys.exit('\n' + table + ' in ' + database + ' does not exist.\n')
    return tables