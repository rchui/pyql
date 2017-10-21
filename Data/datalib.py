""" datalib.py

This file defines functions that deal with data handling.
"""

import sys
from pathlib import Path

def get_tables(database):
    """ Gets the list of tables in the database.

    Args:
        database: the name of the database.

    Returns:
        tables: the tables of the database.
    """
    with open(database) as db_file:
        tables = {}
        for line in db_file:
            table = line.strip()
            if Path(table).is_file(): # Check for table existence.
                tables[table.split('.')[0]] = table.split('.')[1]
            else: # Else exit.
                sys.exit('\n' + table + ' in ' + database + ' does not exist.\n')
    return tables

def get_attributes(tables):
    """ Gets the list of attributes for each table in the database.

    Args:
        tables: the name of the tables.

    Returns:
        attributes: the attributes for all the tables.
    """
    attributes = {}
    for name, file_type in tables.items():
        table = name + '.' + file_type
        with open(table) as relation:
            attributes[name] = relation.readline().strip().split(',')
    return attributes
