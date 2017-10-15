""" pyql.py

This file defines the main body of the pyql query process.
"""

import sys
from Interface.help import print_help
from Interface.choosedb import choose

def main():
    """ The main body of the pyql query process"""
    database = choose().replace('.db', '') + '.db'
    print(database)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print_help()
    main()
