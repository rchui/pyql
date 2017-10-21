""" querylib.py

This file defines functions for querying the database tables.
"""

import sys
from Interface.helplib import query_options, print_tables, print_attributes, print_query

def query(tables, attributes):
    """ Main body of the query loop.

    Args:
        tables: names of the tables in the database.
        attributes: attributes of each table.

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
            print_attributes(attributes)
        elif sub_query == 'query':
            print_query(query_statement)
        elif sub_query == 'clear':
            query_statement = ''
        elif sub_query == 'exit':
            sys.exit()
        else:
            query_statement += ' ' + sub_query
    return query_statement

def check_attribute(attribute, tables, attributes):
    """ Checks the validity of an attribute.

    Args:
        attribute: attribute to check
        table: tables in the database
        attributes: attributes in the database

    Returns:
        result: true if valid, else false
    """
    if len(attribute.split('.')) == 2: # If the attribute has an identifier
        pair = attribute.split('.')
        # print(pair)
        if pair[0] not in tables.keys():
            return False
        elif pair[1] not in attributes[pair[0]]:
            return False
    else: # If the attribute does not have an identifier
        result = False
        for _, value in attributes.items():
            if attribute in value:
                result = True
                break
        if not result:
            return result
    return True

def is_number(value):
    """ Checks if a string is a number or not.

    Args:
        value: the string to check

    Returns:
        True: if a number
        False: else
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def check_valid(selects, froms, wheres, tables, attributes):
    """ Checks the validity of the query.

    Args:
        selects: select values
        froms: from values
        where: where values
        tables: tables in the database
        attributes: attributes of the tables in the database.

    Returns:
        Boolean: true if valid, false else
    """
    # Check validity of tables
    for table in froms:
        print(table)
        if table not in tables.keys():
            return False

    # Check validty of attributes
    for attribute in selects:
        print(attribute)
        if not check_attribute(attribute, tables, attributes):
            return False

    # TODO: wheres validity


    return True
