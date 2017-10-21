""" dblib.py

This file defines functions that create new databases, check for the existence
of databases, scans for potential databases, and chooses from potential
databases.
"""

import sys
import glob
from pathlib import Path

def create(database):
    """ Create a new database.

    Args:
        database: name of the new database.

    Returns:
        database: name of the new database.
     """
    database = database.replace('.db', '')
    tables = []
    print('\nTables to include in ' + database + ' (press enter to close):')
    while True:
        table = input('  > ')
        if table == '': # Exit when no table entered.
            break
        else:
            if Path(table).is_file(): # Check for table existence.
                if table not in tables: # Check for table uniqueness.
                    tables.append(table)
                else:
                    print(table + ' is already in the database.')
            else:
                print(table + ' does not exist.')
    with open(database + '.db', 'w') as file:
        for table in tables:
            file.write(table + '\n')
    return database + '.db'


def check(database):
    """ Checks if the selected database exists.

    Args:
        database: name of the database.

    Returns:
        database: name of the database.
    """
    if Path(database).is_file(): # Database found.
        return database
    else: # Database not found.
        sys.exit('\n' + database + ' does not exist.\n')

def choose(db_files):
    """ Choose a database to load.

    Args:
        None

    Returns:
        database: name of the database.
    """
    while True:
        print('\nWhich database should be used?')
        database = input('  > ') + '.db'
        if database in db_files:
            break
        else:
            print('\nInvalid database choice, please choose again.')
    return database

def scan():
    """ Scans for potential databases.

    Args:
        database: name of database

    Returns:
        database: name of database"""
    db_files = glob.glob('*.db')
    num_dbs = len(db_files)
    if len(db_files) > 1: # More than one database exists.
        print('\nThere are ' + str(len(db_files)) + ' databases in the directory.')
        for file in db_files:
            print('  ' + file.replace('.db', ''))
        database = choose(db_files)
    elif num_dbs == 0: # No databases exist.
        sys.exit('\nNo databases found. Please create one.\n')
    else: # Only one exists.
        database = db_files[0]
    return database
