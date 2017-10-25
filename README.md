# pyql
pyql is an ad-hoc data computing platform that can be used to perform SQL-based queries on data files in the CSV format. It supports SELECT-FROM-WHERE queries, a subset of SL, taking the form where R1, ..., Rm are some tables in the database, A1, ..., An are attributes from these tables, and C1, ..., Ck are simple atomic conditions of the form Ai op value, or Ai op Aj, for attributes Ai, Aj and comparison operator op.

    SELECT A1, ..., An
    FROM R1, ..., Rm
    WHERE C1 AND ... AND Ck

## Operators

    =, >, <, <>, >=, <= for all data types except Boolean.
    LIKE operator for Text. 
    AND, OR, NOT for Boolean.

## Usage
    pyql.py [-h] [-d DATABASE] [-n DATABASE]

## Optional Arguments
    -h, --help                          show this help message and exit
    -d DATABASE, --database DATABASE    database to query from
    -n DATABASE, --new DATABASE         create a new database