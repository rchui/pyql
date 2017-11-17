""" tablelib.py

This file defines functions for getting table information.
"""

SWAP = {'>=': '<',
        '<=': '>',
        '<>': '=',
        '=': '<>',
        '<': '>=',
        '>': '<=',
        'like': 'like'}

def get_where_indexes(wheres, attributes):
    """ Gets the indexes for all where statements.

    Args:
        wheres: where values
        attributes: attributes in the tables

    Returns:
        indexes: look up indexes for where values.
    """
    indexes = []
    for where in wheres:
        if len(where) == 3:
            subresult = [element.split('.') for element in where]
            for i in range(len(subresult)):
                if len(subresult[i]) == 2:
                    subresult[i][1] = attributes[subresult[i][0]].index(subresult[i][1])
            indexes.append(subresult)
        else:
            indexes.append(where)
    return indexes

def get_select_indexes(selects, attributes):
    """ Gets the indexes for all select statements.

    Args:
        selects: select values
        attributes: attributes in the tables

    Returns:
        indexes: look up indexes for select values
    """
    if selects[0] != '*':
        indexes = []
        split_select = [select.split('.') for select in selects]
        for select in split_select:
            indexes.append([select[0], attributes[select[0]].index(select[1])])
        return indexes
    else:
        return [selects]

def get_conditions(wheres):
    conditions = {}
    swap = False
    for where in wheres:
        if where[0] == 'not':
            swap = True
        if len(where) == 3 and not (len(where[0]) == 2 and len(where[2]) == 2):
            if len(where[0]) == 2:
                if where[0][0] not in conditions.keys():
                    conditions[where[0][0]] = []
                conditions[where[0][0]].append([where[0][1], where[1][0], where[2][0]])
            else:
                if where[2][0] not in conditions.keys():
                    conditions[where[2][0]] = []
                conditions[where[2][0]].append([where[2][1], where[1],[0], where[0][0]])
            if swap:
                conditions[where[2][0]][-1][1] = SWAP[conditions[where[2][0]][-1][1]]
                swap = False
    return conditions
