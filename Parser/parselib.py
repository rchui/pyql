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
        None
    """
    print_query(query)
    parsed_query = sqlparse.parse(query)[0]
    tokens = [str(token) for token in parsed_query if str(token) != ' ']
    selects = [token.strip() for token in tokens[1].split(',')]
    froms = [token.strip() for token in tokens[3].split(',')]

    # Don't ask what this does. It just works lol.
    wheres = [[subtoken.strip() for subtoken in re.split(r'(>=|<=|<>|=|<|>)', token.strip())]
              for token in re.split(r'(and|or|not|AND|OR|NOT)', re.sub(r'(where|WHERE|;)', '', tokens[-1])
                                    .replace("'", '')
                                    .strip())]

    return selects, froms, wheres
