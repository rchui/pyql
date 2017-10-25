""" pyql.py

This file defines the main body of the pyql query process.
"""

import argparse
from Interface.dblib import create, check, scan
from Interface.helplib import print_header
from Query.querylib import query, get_query, check_valid
from Data.datalib import get_tables, get_attributes
from Data.tablelib import get_where_indexes, get_select_indexes
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
    db_attributes = get_attributes(tables)

    while True:
        pool = []
        query_statement = get_query(tables, db_attributes) # Build query
        selects, froms, wheres, tables, attributes, parse_valid = parse_query(query_statement, tables, db_attributes) # Parse query
        if parse_valid:
            if check_valid(selects, froms, wheres, tables, attributes): # Check query validity
                wheres = get_where_indexes(wheres, attributes) # Get where indexes
                selects = get_select_indexes(selects, attributes) # Get select indexes
                print_header(selects, attributes, froms)
                query(0, selects, froms, wheres, tables, {}, pool) # Query tables
            else:
                print('\nInvalid query.')
        for process in pool:
            process.join()

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
