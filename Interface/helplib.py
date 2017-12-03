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
    print('  index       create an index')
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

def print_divider(output):
    """ Prints a divider between the labels and results.

    Args:
        output: output to print

    Returns:
        None
    """
    flat_output = []
    for sublist in output:
        for item in sublist:
            flat_output.append(item)
    for i in range(13):
        print('-', end='')
    for i in range(len(flat_output)):
        if i != 0:
            print('|', end='')
            for _ in range(14):
                print('-', end='')
    print()

def print_output(output):
    """ Prints the query results.

    Args:
        output: output to print

    Returns:
        None
    """
    flat_output = []
    for sublist in output:
        for item in sublist:
            flat_output.append(item)
    print('{:12.12}'.format(flat_output[0]), end='')
    for i in range(len(flat_output)):
        if i != 0:
            print(' | {:12.12}'.format(flat_output[i]), end='')
    print()

def print_header(selects, attributes, froms):
    """ Prints the query result header.

    Args:
        selects: select values
        attributes: attributes in the tables
        froms: from values

    Returns:
        None
    """
    if selects[0][0] == '*':
        if len(froms[0]) == 2:
            output = [[table[1] + '.' + element for element in attributes[table[1]]]
                      for table in froms]
        else:
            output = [[table[0] + '.' + element for element in attributes[table[0]]]
                      for table in froms]
    else:
        output = [[select[0] + '.' + attributes[select[0]][select[1]]]
                  for select in selects]
    print()
    print_output(output)
    print_divider(output)
