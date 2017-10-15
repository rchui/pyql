""" choosedb.py

This file defines the user interface for choosing a database.
"""

import sys
import glob
from pathlib import Path
from Interface.createdb import create

def create_load(database):
    """ Create new database or load existing.

    Args:
        database: name of database to load or create

    Returns:
        database: name of database to load or create
    """
    if sys.argv[1] == 'new': # Createa a new database.
        print('\nBuilding new database ' + sys.argv[2])
        create(sys.argv[2])
        sys.exit('')
    elif '.db' in sys.argv[1]: # Search for given database.
        if Path(sys.argv[1]).is_file(): # Database found.
            database = sys.argv[1]
        else: # Database not found.
            sys.exit('\n' + sys.argv[1] + ' does not exist.\n')
    else: # Was not given a .db file name.
        sys.exit('\nIncorrect options given.\n')
    return database

def scan_potential(database):
    """ Scans for databases.

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
        while True:
            print('\nWhich database should be used?')
            database = input('  > ') + '.db'
            if database in db_files:
                break
            else:
                print('\nInvalid database choice, please choose again.')
    elif num_dbs == 0: # No databases exist.
        sys.exit('\nNo databases found. Please create one.\n')
    else: # Only one exists.
        database = db_files[0]
    return database

def choose():
    """ Choose an existing datbase or create a new database. """
    database = ''
    if len(sys.argv) > 1: # Manually loading or creating new database.
        database = create_load(database)
    else: # Scan for potential databases.
        database = scan_potential(database)

    print('\nLoading ' + database.replace('.db', '') + ' database')
    return database
