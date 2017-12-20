""" tablelib.py

This file defines functions for getting table information.
"""

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


def get_table_size(tables):
    """ Gets the tables size of all tables in the database.
    
    Args:
        tables: tables in the database

    Returns:
        None
    """
    line_counts={}
    for table, ext in tables.items():
        i=0
        with open(table+'.'+ext) as fh:
            for line in fh:
                i+=1
        line_counts[table]=i
    return line_counts
