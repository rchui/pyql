""" parselib.py

This file defines functions that parse the SQL queries.
"""

import re
import imp
try:
    imp.find_module('sqlparse')
except ImportError:
    from subprocess import call
    print('\nsqlparse not found. Attempting sqlparse installation.')
    call(['pip3', 'install', 'sqlparse'])
import sqlparse

def print_query(query):
    """ Beautified print of the given query

    Args:
        query: query to print

    Returns:
        None
    """
    print(sqlparse.format(query, reindent=True, keyword_case='upper'))

def parse_query(query):
    """ Parse the given query

    Args:
        query: query to parse

    Returns:
        selects: select values
        froms: from values
        wheres: where values
    """
    try:
        print_query(query)
        # Parse the SQL query
        parsed_query = sqlparse.parse(query)[0]
        # Split into tokens
        tokens = [str(token) for token in parsed_query if str(token) != ' ']
        # Get select values
        selects = [token.strip() for token in tokens[1].split(',')]
        # Get from values
        froms = [token.strip() for token in tokens[3].split(',')]
        # Get where values
        # Don't ask what this does. It just works lol.
        wheres = [[subtoken.strip() for subtoken in re.split(r'(>=|<=|<>|=|<|>|like|LIKE)', token.strip())]
                  for token in re.split(r'(and|or|not|AND|OR|NOT)',
                                        re.sub(r'(where|WHERE|;|\'|‘|")', '', tokens[-1])
                                        .strip())]

        for i in range(0, len(wheres), 2):
            wheres[i][1] = wheres[i][1].lower()
        for i in range(1, len(wheres), 2):
            wheres[i] = [wheres[i][0].lower()]

        # print(selects)
        # print(froms)
        # print(wheres)

        return selects, froms, wheres, True
    except:
        print('\nInvalid query.')
        return selects, froms, wheres, False
