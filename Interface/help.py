""" help.py

This file defines the help text for pyql.
"""

import sys

def print_help():
    """ Prints help text. """
    print('\n\
pyql - Python Query Language\n\
\n\
Options:\n\
    python pyql.py                # Scan for databases.\n\
    python pyql.py new <database> # Create new database.\n\
    python pyql.py <database.db>  # Load a database.db.\n\
')
    sys.exit()
