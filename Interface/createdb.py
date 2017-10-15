""" createdb.py 

This files defines the database creation process.
"""

from pathlib import Path

def create(database):
    """ Create a new database.
    
    Args:
        database: name of the new database.

    Returns:
        None
     """
    database = database.replace('.db', '')
    tables = []
    print('\nTables to include in ' + database + ' (press enter to close):')
    while True:
        table = input('  > ')
        if table == '':
            break
        else:
            if Path(table).is_file():
                tables.append(table)
            else:
                print(table + ' does not exist.')
    with open(database + '.db', 'w') as file:
        for table in tables:
            file.write(table + '\n')
