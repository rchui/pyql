""" querylib.py

This file defines functions for querying the database tables.
"""

import sys
import csv
from multiprocessing import Process
import Logic.bool_compare as bc
from Interface.helplib import query_options, print_tables, print_attributes, print_query, print_output

OPERATORS = ['>=', '<=', '<>', '=', '<', '>', 'like']
BOOLEAN = ['and', 'or', 'not']

def compare(first, second, operator):
    """ Compare two values.

    Args:
        first: first value
        second: second value

    Returns:
        Boolean result of comparison.
    """
    if operator == '=':
        return bc.equal(first, second)
    elif operator == '<=':
        return bc.less_than_or_equal(first, second)
    elif operator == '>=':
        return bc.greater_than_or_equal(first, second)
    elif operator == '<>':
        return bc.not_equal(first, second)
    elif operator == '<':
        return bc.less_than(first, second)
    elif operator == '>':
        return bc.greater_than(first, second)
    elif operator == 'like':
        return bc.like(first, second)
    else:
        print('\nIncorrect operator ' + operator + ' included in query.')

def check_and_print(wheres, lines, selects, froms):
    """ Checks if the current line meets the where conditions.

    Args:
        wheres: where values
        lines: current cartesian line product
        selects: select values
        froms: from values

    Returns:
        None
    """
    if len(wheres) != 0:
        results = [None] * len(wheres)
        for i in range(len(wheres)):
            if len(wheres[i]) == 3: # Boolean comparison
                if len(wheres[i][0]) == 2: # Get first value
                    first = lines[wheres[i][0][0]][wheres[i][0][1]]
                else:
                    first = wheres[i][0][0]
                if len(wheres[i][2]) == 2: # Get second value
                    second = lines[wheres[i][2][0]][wheres[i][2][1]]
                else:
                    second = wheres[i][2][0]
                results[i] = compare(first, second, wheres[i][1][0])
            else:
                results[i] = wheres[i][0]

        # Flip all values after not then remove
        for i in range(len(results)):
            if results[i] == 'not':
                results[i + 1] = not results[i + 1]
        results = list(filter(('not').__ne__, results))

        # Build result
        is_valid = results[0]
        for i in range(1, len(results), 2):
            if results[i] == 'and':
                is_valid = is_valid and results[i + 1]
            elif results[i] == 'or':
                is_valid = is_valid or results[i + 1]
    else:
        is_valid = True
    sys.stdout.flush()

    # Print result
    if is_valid:
        if selects[0][0] == '*':
            if len(froms[0]) == 2:
                output = [lines[table[1]] for table in froms]
            else:
                output = [lines[table[0]] for table in froms]
        else:
            output = [[lines[select[0]][select[1]]] for select in selects]
        print_output(output)

def query(reader_num, selects, froms, wheres, tables, attributes, indexes, lines, comparisons):
    """ Main body of the query loop.

    Args:
        reader_num: current reader number
        selects: select values
        froms: from values
        wheres: where values
        tables: tables in the database.
        lines: current line from each reader
        comparisons: attribute to compare

    Returns:
        None
    """
    if reader_num != len(froms): # Recursively open readers for cartesian product.
        if tables[froms[reader_num][0]] == 'idx': # Table is an index
            rules = []
            alias = froms[reader_num]
            index = indexes[alias[0]][1]

            # Get all conditions that are relavent
            for comp in comparisons[alias[1]]:
                if reader_num == 0:
                    if len(comp) == 2 and attributes[alias[1]][comp[0]] == indexes[alias[0]][0]:
                        rules.append(comp)
                else:
                    if attributes[alias[1]][comp[0]] == indexes[alias[0]][0]:
                        rules.append(comp)
            with open(indexes[alias[0]][2], 'r') as file_reader:
                file_reader.readline()
                if len(rules) == 0: # No rules so check every line
                    for line in csv.reader(file_reader):
                        if len(froms[0]) == 2:
                            lines[froms[reader_num][1]] = line
                        else:
                            lines[froms[reader_num][0]] = line
                        query(reader_num + 1, selects, froms, wheres, tables, attributes, indexes, lines, comparisons)
                else: # There are rules
                    position_set = set()

                    # Look up value in index.
                    # Seek to position.
                    # Readline, split and recurse.
                    for rule in rules:
                        if len(rule) == 2: # There are 2 length rules
                            try:
                                for position in index[rule[1]]:
                                    if position not in position_set:
                                        position_set.add(position)
                                        file_reader.seek(position, 0)
                                        line = file_reader.readline().strip().split(',')
                                        if len(froms[0]) == 2:
                                            lines[froms[reader_num][1]] = line
                                        else:
                                            lines[froms[reader_num][0]] = line
                                        query(reader_num + 1, selects, froms, wheres, tables, attributes, indexes, lines, comparisons)
                            except:
                                pass
                        else: # There are 3 length rules
                            if froms[reader_num - 1][1] == rule[1]:
                                try:
                                    for position in index[lines[froms[reader_num - 1][1]][rule[2]]]:
                                        if position not in position_set:
                                            position_set.add(position)
                                            file_reader.seek(position, 0)
                                            line = file_reader.readline().strip().split(',')
                                            if len(froms[0]) == 2:
                                                lines[froms[reader_num][1]] = line
                                            else:
                                                lines[froms[reader_num][0]] = line
                                            query(reader_num + 1, selects, froms, wheres, tables, attributes, indexes, lines, comparisons)
                                except:
                                    pass
        else: # Table is not an index
            with open(froms[reader_num][0] + '.' + tables[froms[reader_num][0]]) as file_reader:
                file_reader.readline() # Throw away first line
                for line in csv.reader(file_reader):
                    if len(froms[0]) == 2:
                        lines[froms[reader_num][1]] = line
                    else:
                        lines[froms[reader_num][0]] = line
                    query(reader_num + 1, selects, froms, wheres, tables, attributes, indexes, lines, comparisons)
    else: # All readers open, analyze all line combinations.
        check_and_print(wheres, lines, selects, froms)

def make_index(tables, attributes, indexes):
    """ Makes an index.

    Args:
        None

    Returns:
        None
    """
    print()
    name = input('  CREATE INDEX ')
    table = input('  ON ')
    attribute = input('  FOR ')

    with open(table + '.csv', 'r') as f:
        with open(table + '.csv', 'r') as f_2:
            # Split header
            header = f.readline().strip().split(',')
            f_2.readline()

            # Look up attribute index
            tab = csv.reader(f, delimiter=',')
            column = header.index(attribute)
            index = {}

            # Gather dictionary of lists of tell positions
            for row in tab:
                key = row[column]
                if key in index.keys():
                    index[key].append(f_2.tell())
                else:
                    index[key] = [f_2.tell()]
                f_2.readline()

    tables[name] = 'idx'
    attributes[name] = attributes[table]
    indexes[name] = [attribute, index, table + '.csv']
    print()

def get_query(tables, attributes, indexes):
    """ Main body of the query building loop.

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
        if sub_query.strip() != '':
            if sub_query == 'help':
                query_options()
            elif sub_query == 'tables':
                print_tables(tables)
            elif sub_query == 'attributes':
                print_attributes(attributes)
            elif sub_query == 'index':
                make_index(tables, attributes, indexes)
            elif sub_query == 'query':
                print_query(query_statement)
            elif sub_query == 'clear':
                query_statement = ''
            elif sub_query == 'exit':
                sys.exit()
            else:
                query_statement += ' ' + sub_query
    return query_statement

def check_attribute(attribute, attributes):
    """ Checks the validity of an attribute.

    Args:
        attribute: attribute to check
        attributes: attributes in the database

    Returns:
        result: true if valid, else false
    """
    if len(attribute.split('.')) == 2: # If the attribute has an identifier
        pair = attribute.split('.')
        # print(pair)
        if pair[0] not in attributes.keys():
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
        if table[0] not in tables.keys():
            return False

    # Check validty of attributes
    if selects[0] != '*':
        for attribute in selects:
            if not check_attribute(attribute, attributes):
                return False

    # Check validity of where statements
    for i in range(len(wheres)):
        if len(wheres[i]) == 3:
            if wheres[i][1].lower() not in OPERATORS:
                return False
            if '.' in wheres[i][0]:
                if not check_attribute(wheres[i][0], attributes):
                    return False
            if '.' in wheres[i][2]:
                if not check_attribute(wheres[i][0], attributes):
                    return False
        elif len(wheres[i]) == 1:
            if wheres[i][0] not in BOOLEAN:
                return False
    return True
