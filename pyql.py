""" pyql.py

This file defines the main body of the pyql query process.
"""

import argparse
from Interface.dblib import create, check, scan
from Query.querylib import query, get_query, check_valid
from Data.datalib import get_tables, get_attributes
from Parser.parselib import parse_query

FLAGS = None
"""
    new: the name of the new database.
    database: the name of the database to query.
"""

def main():
    """ The main body of the pyql query process

    Args:
        argv: user passed arguments.

    Returns:
        None
    """
    database = ''
    if FLAGS.new != '': # Create a new database.
        database = create(FLAGS.new)
    elif FLAGS.database != '': # Load an existing database.
        database = check(FLAGS.database)
    else: # Choose a potenital database if none provided.
        database = scan()
    tables = get_tables(database)
    attributes = get_attributes(tables)

    print(tables)
    print(attributes)

    while True:
        query_statement = get_query(tables, attributes)
        selects, froms, wheres, parse_valid = parse_query(query_statement)
        if parse_valid:
            if check_valid(selects, froms, wheres, tables, attributes):
                query(0, selects, froms, wheres, tables, attributes, {})
            else:
                print('\nInvalid query.')

if __name__ == '__main__':
    # Create argument parser.
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        '-d', '--database',
        type=str,
        default='',
        help='query database with given name'
    )
    PARSER.add_argument(
        '-n', '--new',
        metavar='DATABASE',
        type=str,
        default='',
        help='create a new database with given name'
    )

    # Gather arguments.
    FLAGS, _ = PARSER.parse_known_args()

    # Start program.
    main()
