#!/usr/bin/python

import pandas as pd
import csv

filename = 'review-5k.csv'
col = 'user_id'

def getDict(filename, col):
    """Generate a dictionary given table and column name.
    
       parameters: filename -- file to open
                   col      -- name of column to grab values from"""

    with open(filename, 'r') as f:
        with open(filename, 'r') as f_2:
            header = f.readline().split(',')
            f_2.readline()
        
            table = csv.reader(f, delimiter=',')
            column = header.index(col)
            index = {}
        
            for row in table:
                key = row[column]
                if key in index.keys():
                    index[key].append(f_2.tell())
                else:
                    index[key] = [f_2.tell()]
                f_2.readline()
        print(index)

getDict(filename, col)


