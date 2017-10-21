""" helplib.py

This file defines functions that provide help.
"""

def query_options():
    """ Prints the different query options.

    Args:
        None

    Returns:
        None
    """
    print('\nOptions:')
    print()
    print('  tables      get database tables')
    print('  attributes  get attributes for each table')
    print('  query       get the current query')
    print('  clear       clear the current query')
    print('  exit        exit pyql')
    print()

def print_tables(tables):
    """ Prints the tables for the database.

    Args:
        tables: tables to print.

    Returns:
        None
    """
    print('\n', tables, '\n')

def print_attributes(attributes):
    """ Prints the attributes for each table.

    Args:
        attributes: attributes to print.

    Returns:
        None
    """
    print('\nAttributes:\n')
    for key, value in attributes.items():
        print(key + ':')
        print(value, '\n')

def print_query(query):
    """ Prints the current query.

    Args:
        query: query to print.

    Returns:
        None
    """
    print('\n', query, '\n')
