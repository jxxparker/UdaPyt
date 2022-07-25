--  26 ) Creating a database - P1

--  CREATE DATABASE [IF NOT EXISTS] database_name;

--  CREATE DATABASE : creates a dabase as an abstract unit

--  [IF NOT EXISTS] : verifies if a database with the same name exists already.
--  	- the brackets around mean the statement is optional( you could either type or omit the statement)

--  database_name : give a name that is short but at the same time as related to the content as possible.
-- 	- the sql code is not case sensitive
--  - in this elemtn the quotes are optional

-- the semicolon character : it functions as a statement terminator
-- 	- whenyour code contains more than a single statement, ; is indispensable.

CREATE DATABASE IF NOT EXISTS Sales; 
CREATE SCHEMA IF NOT EXISTS Sales;

USE Sales;
