""" query.py

This file defines the query class.
"""

class Query:
    """ Query class that holds query options."""
    def __init__(self):
        self.q_select = []
        self.q_from = []
        self.q_where = []
