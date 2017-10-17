""" printerlib.py

This file defines functions to print the data.
"""

import pprint as pp
import numpy as np

def print_sum(data):
    """ Prints a summary of the data.

    Args:
        data: data to print.

    Returns:
        None
    """
    print(np.array(data))

def print_all(data):
    """ Prints all of the data.

    Args:
        data: data to print.

    Returns:
        None
    """
    pp.pprint(data)
