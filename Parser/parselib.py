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
    wheres = [[subtoken.strip() for subtoken in re.split(r'(>=|<=|<>|=|<|>)', token.strip())]
              for token in re.split(r'(and|or|not|AND|OR|NOT|like|LIKE)',
                                    re.sub(r'(where|WHERE|;)', '', tokens[-1])
                                    .replace("'", '')
                                    .strip())]

    return selects, froms, wheres
