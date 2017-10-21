"""
This file contains the functions for the SQL opertators to evaluate subqueries in the WHERE statements
"""
import re

#check if either of the two input strings is actually a float data structre, and convert if so. This function is called in each comparison operator function
def is_float(num1, num2):
    try:
        num1 = float(num1)
    except:
        pass
    try:
        num2 = float(num2)
    except:
        pass
    return num1, num2


#return boolean value for '=' operator
def equal(v1,v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery

    Returns:
        boolean value for SQL equal comparison, =
    """

    v1, v2 = is_float(v1, v2)
    return v1 == v2


def less_than_or_equal(v1, v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery
    
    Returns:
        boolean value for SQL less than or equal comparison, <=
    """

    v1, v2 = is_float(v1, v2)
    if type(v1) != type(v2): #will never be true 
        return False
    else:
        return v1 <= v2


def greater_than_or_equal(v1, v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery

    Returns:
        boolean value for SQL greater than or equal comparison, >=
    """

    v1, v2 = is_float(v1, v2)
    if type(v1) != type(v2):
        return False
    else:
        return v1 >= v2


def not_equal(v1, v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery

    Returns:
        boolean value for SQL not equal comparison, <>
    """

    v1, v2 = is_float(v1, v2)
    return v1 != v2


def less_than(v1, v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery

    Returns:
        boolean value for SQL less than comparison, >
    """

    v1, v2 = is_float(v1, v2)
    if type(v1) != type(v2):
        return False
    else:
        return v1 < v2


def greater_than(v1, v2):
    """
    Args:
        v1: first string in WHERE subquery
        v2: second string in WHERE subquery

    Returns:
        boolean value for SQL greater than comparison, >
    """

    v1, v2 = is_float(v1, v2)
    if type(v1) != type(v2):
        return False
    else:
        return v1 > v2



def like(v1, v2):
    """
    return boolean value with the like comparison operator
    assumes that v1 is beings compared with LIKE to v2
    %: any string
    _: any character
    """

    v2 = v2.replace('%', '.+') #convert SQL any string to 1 or more characters in regex
    v2 = v2.replace('_', '.') #convert SQL any character to 1 charachter in regex
    pattern = re.compile(v2) #match object will exist only if pattern matches
    match = pattern.match(v1)
    if match:
        return True
    else:
        return False

