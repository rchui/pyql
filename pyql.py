""" pyql.py

This file defines the main body of the pyql query process.
"""

import sys
import argparse
from Interface.dblib import create, check, scan

FLAGS = None

def main(argv):
    """ The main body of the pyql query process"""
    database = ''
    if FLAGS.new != '': # Create a new database.
        database = create(FLAGS.new)
    elif FLAGS.database != '': # Load an existing database.
        database = check(FLAGS.database)
    else: # Choose a potenital database if none provided.
        database = scan()

if __name__ == '__main__':
    # Create argument parser.
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        '-d', '--database',
        type=str,
        default='',
        help='Database to query from.'
    )
    PARSER.add_argument(
        '-n', '--new',
        type=str,
        default='',
        help='Create a new database.'
    )

    # Gather arguments.
    FLAGS, UNPARSED = PARSER.parse_known_args()
    main(argv=[sys.argv[0]] + UNPARSED)
