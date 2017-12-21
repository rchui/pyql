# pyql - Python Query Language
pyql is an ad-hoc data computing platform that can be used to perform SQL-based queries on data files in the CSV format. It supports SELECT-FROM-WHERE queries, a subset of SL, taking the form where R1, ..., Rm are some tables in the database, A1, ..., An are attributes from these tables, and C1, ..., Ck are simple atomic conditions of the form Ai op value, or Ai op Aj, for attributes Ai, Aj and comparison operator op.

    SELECT A1, ..., An
    FROM R1, ..., Rm
    WHERE C1 AND ... AND Ck

## Operators

* =, >, <, <>, >=, <= for all data types except Boolean.
* LIKE operator for Text. 
* AND, OR, NOT for Boolean.

## Usage
    pyql.py [-h] [-d DATABASE] [-n DATABASE]

## Prepare input
Database file: database.db
List each one csv file per line, each csv file is a table in the database
See test.db for example

## Optional Arguments
    -h, --help                          show this help message and exit
    -d DATABASE, --database DATABASE    database to query from
    -n DATABASE, --new DATABASE         create a new database

## Example and Notes
    # Make a new database and follow directions to add csv files.
    # When adding csv files include '.csv'
    > python3 pyql -n yelp
    > business.csv
    > review-1m.csv
    > photos.csv
    >

    # To make indexes specify index name, table, and attribute
    # When entering tables don't include '.csv'
    # Attributes should be the same as in the table. Type 'attributes' to see them.
    > index

    CREATE INDEX review_idx
    FOR review-1m
    ON stars

    # Query on the index created.
    # Always use an alias and do not use quotes ', " unless denoting empty space like '' or "".
    > SELECT R.review_id, R.stars, R.useful FROM review_idx R WHERE R.stars >= 4 AND R.useful > 20;

    # Note that we don't support the join statement.
    # Instead, declare two tables and the join in the WHERE clause
    > SELECT ... FROM review R JOIN Business B ON (B.id = R.id) WHERE ...
    # To
    > SELECT ... FROM review R, Business B WHERE B.id = R.id AND ...