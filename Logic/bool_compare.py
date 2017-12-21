""" bool_compare.py

This file contains the functions for the SQL opertators to evaluate subqueries
in the WHERE statements.
"""

import re


def check_if_date(date_string):
    """
    Check if a string is a date in the format YYYY/MM or YYYY/MM/DD"

    Args: a string value in the

    Returns: True or False
    """
    if '-' in date_string:
        date_string=date_string.replace('-', '/')

    try:
        date_string=date_string.split('/')

        if len(date_string[0])==2 and len(date_string[1])==2 and len(date_string[2])==4:
            try:
                float_test=[float(x) for x in date_string]
                if float_test[0] > 12 or float_test[0] < 1:
                    return False

                if float_test[1] > 31 or float_test[1] < 1:
                    return False

                return True
            except:
                return False

        elif len(date_string[0])==4 and len(date_string[1])==2 and len(date_string[2])==2:
            try:
                float_test=[float(x) for x in date_string]
                if float_test[1] > 12 or float_test[1] < 1:
                    return False

                if float_test[2] > 31 or float_test[2] < 1:
                    return False

                return True
            except:
                return False

        else:
            return False

    except:
        return False
    

def parse_date(date_string):
    """ Parses the date given a particular date string.
    
    Args:
        date_string: the date to be parsed.

    Returns:
        Uniformly formatted date_string.
    """
    if '-' in date_string:
        date_string=date_string.replace('-', '/')
    date_string=date_string.split('/')
    if len(date_string[0])==2:
        return date_string[2]+'/'+date_string[0]+'/'+date_string[1]
    else:
        return date_string[0]+'/'+date_string[1]+'/'+date_string[2]

#print(parse_date('12-13-1999'))


def is_float(num1, num2):
    """
    Check if either of the two input strings is actually a float data structre,
    and convert if so.

    Args:
        num1: first string in WHERE subquery
        num2: second string in WHERE subquery

    Returns:
        tuple of inputs converted to float if possible, or string
    """
    try:
        num1 = float(num1)
    except:
        pass
    try:
        num2 = float(num2)
    except:
        pass
    return num1, num2


def equal(value1, value2):
    """
    Check if the two values are equal.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL equal comparison, =
    """

    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)
    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 == value2

    elif v1_date_check or v2_date_check:
        return False

    value1, value2 = is_float(value1, value2)
    return value1 == value2


def less_than_or_equal(value1, value2):
    """
    Check if the first value is less than or equal to the second.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL less than or equal comparison, <=
    """
    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)


    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 <= value2

    elif v1_date_check or v2_date_check:
        return False


    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2): #will never be true
        return False
    else:
        return value1 <= value2


def greater_than_or_equal(value1, value2):
    """
    Check if the first value is greater than or equal to the second.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL greater than or equal comparison, >=
    """
    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)

    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 >= value2

    elif v1_date_check or v2_date_check:
        return False

    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 >= value2


def not_equal(value1, value2):
    """
    Checks if the values are not equal.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL not equal comparison, <>
    """
    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)

    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 != value2

    elif v1_date_check or v2_date_check:
        return False

    value1, value2 = is_float(value1, value2)
    return value1 != value2


def less_than(value1, value2):
    """
    Checks if the first value is less then the second.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL less than comparison, >
    """

    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)

    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 < value2

    elif v1_date_check or v2_date_check:
        return False


    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 < value2


def greater_than(value1, value2):
    """
    Checks if the first value is greater than the second.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value for SQL greater than comparison, >
    """

    v1_date_check = check_if_date(value1)
    v2_date_check = check_if_date(value2)


    if v1_date_check and v2_date_check:
        value1, value2 = parse_date(value1), parse_date(value2)
        return value1 > value2

    elif v1_date_check or v2_date_check:
        return False


    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 > value2



def like(value1, value2):
    """
    Checks if the first value is SQL-like the second.

    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery

    Returns:
        boolean value with the like comparison operator

    Notes
        %: any string
        _: any character
    """

    value2 = value2.replace('%', '\.*') #convert SQL any string to 1 or more characters in regex
    value2 = value2.replace('_', '\.') #convert SQL any character to 1 character in regex
    pattern = re.compile(value2)
    match = pattern.search(value1) #match object will exist only if pattern matches
    return match != None
