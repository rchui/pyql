""" querylib.py

This file defines functions for querying the database tables.
"""

import sys
from Interface.helplib import query_options, print_tables, print_attributes, print_query

def query(tables):
    """ Main body of the query loop.

    Args:
        tables: names of the tables in the database.

    Returns:
        query_statement: the query to process.
    """
    print('\nEnter query or type "help" for options.')
    query_statement = ''
    while not query_statement.endswith(';'):
        sub_query = input('  > ')
        if sub_query == 'help':
            query_options()
        elif sub_query == 'tables':
            print_tables(tables)
        elif sub_query == 'attributes':
            print_attributes(tables)
        elif sub_query == 'query':
            print_query(query_statement)
        elif sub_query == 'clear':
            query_statement = ''
        elif sub_query == 'exit':
            sys.exit()
        else:
            query_statement += ' ' + sub_query
    return query_statement
