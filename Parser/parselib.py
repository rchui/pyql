""" parselib.py

This file defines functions that parse the SQL queries.
"""

import re
import sqlparse

def parse_comparisons(wheres, comparisons):
    """ Get all the equality comparisons """
    for where in wheres:
        if len(where) == 3 and where[1][0] == '=': # =, <>, >, <, >=, <= expanded only for 2 length
            if len(where[0]) == 2:
                if where[0][0] in comparisons.keys():
                    comparisons[where[0][0]].append([where[0][1]] + where[2]) # Change length 3 -> A: [A.#, op, B, B.#], length 2 -> A: [A.#, op, #]
                else:
                    comparisons[where[0][0]] = [[where[0][1]] + where[2]]
            if len(where[2]) == 2:
                if where[2][0] in comparisons.keys():
                    comparisons[where[2][0]].append([where[2][1]] + where[0])
                else:
                    comparisons[where[2][0]] = [[where[2][1]] + where[0]]
    return comparisons

def print_query(query):
    """ Beautified print of the given query

    Args:
        query: query to print

    Returns:
        None
    """
    print(sqlparse.format(query, reindent=True, keyword_case='upper'))

def parse_query(query, tables, db_attributes):
    """ Parse the given query

    Args:
        query: query to parse
        tables: tables in the database
        db_attributes: attributes of tables in the database

    Returns:
        selects: select values
        froms: from values
        wheres: where values
        parse_valid: true if valid, else false
        attributes: attributes of tables in the database
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
        froms = [[subtoken.strip() for subtoken in token.strip().split(' ')] for token in tokens[3].split(',')]
        attributes = {}
        if len(froms[0]) == 2:
            for table in froms:
                attributes[table[1]] = db_attributes[table[0]]
        else:
            attributes = db_attributes
        # Get where values
        # Don't ask what this does. It just works lol.
        wheres = [[subtoken.strip()
                   for subtoken in re.split(r'(>=|<=|<>|=|<|>|LIKE)', token.strip())]
                  for token in re.split(r'(AND|OR|NOT)',
                                        re.sub(r'(WHERE|;|\'|‘|")', '', tokens[-1])
                                        .strip())]
        if [''] in wheres:
            wheres.remove([''])

        # Set operators to lower
        for i in range(len(wheres)):
            if len(wheres[i]) == 3:
                wheres[i][1] = wheres[i][1].lower()
            elif len(wheres[i]) == 1:
                wheres[i] = [wheres[i][0].lower()]
        return selects, froms, wheres, tables, attributes, True
    except Exception as e:
        print('\nInvalid query.')
        return selects, froms, wheres, tables, attributes, False
