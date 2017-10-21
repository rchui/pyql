"""
This file contains the functions for the SQL opertators to evaluate subqueries in the WHERE statements
"""
import re

#check if either of the two input strings is actually a float data structre, and convert if so. This function is called in each comparison operator function
def is_float(num1, num2):
    """
    Check if either of the two input strings is actually a float data structre, and convert if so. This function is called in each comparison operator function
    
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


def equal(value1,value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    
    Returns:
        boolean value for SQL equal comparison, =
    """

    value1, value2 = is_float(value1, value2)
    return value1 == value2


def less_than_or_equal(value1, value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    
    Returns:
        boolean value for SQL less than or equal comparison, <=
    """

    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2): #will never be true 
        return False
    else:
        return value1 <= value2


def greater_than_or_equal(value1, value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    Returns:
        boolean value for SQL greater than or equal comparison, >=
    """

    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 >= value2


def not_equal(value1, value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    Returns:
        boolean value for SQL not equal comparison, <>
    """

    value1, value2 = is_float(value1, value2)
    return value1 != value2


def less_than(value1, value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    Returns:
        boolean value for SQL less than comparison, >
    """

    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 < value2


def greater_than(value1, value2):
    """
    Args:
        value1: first string in WHERE subquery
        value2: second string in WHERE subquery
    Returns:
        boolean value for SQL greater than comparison, >
    """

    value1, value2 = is_float(value1, value2)
    if type(value1) != type(value2):
        return False
    else:
        return value1 > value2



def like(value1, value2):
    """
    return boolean value with the like comparison operator
    assumes that value1 is beings compared with LIKE to value2
    %: any string
    _: any character
    """

    value2=value2.replace('%', '.+') #convert SQL any string to 1 or more characters in regex
    value2=value2.replace('_', '.') #convert SQL any character to 1 charachter in regex
    pattern=re.compile(value2) 
    match=pattern.match(value1) #match object will exist only if pattern matches
    if match:
        return True
    else:
        return False

