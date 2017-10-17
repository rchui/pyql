""" pyql.py

This file defines the main body of the pyql query process.
"""

import sys
import argparse
from Interface.dblib import create, check, scan
from Data.datalib import load

FLAGS = None
"""
    new: the name of the new database.
    database: the name of the database to query.
"""

def main(argv):
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
    tables = load(database)
    print(tables)

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
    FLAGS, UNPARSED = PARSER.parse_known_args()
    main(argv=[sys.argv[0]] + UNPARSED)
