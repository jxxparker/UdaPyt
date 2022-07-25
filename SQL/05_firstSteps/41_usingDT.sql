# 41 Using Database and Tables

CREATE DATABASE IF NOT EXISTS Sales;
USE Sales;
SELECT * FROM customers;
SELECT * FROM sales.customers; 

# queries : one of their main features is to manipulate data within a database
# example : SELECT * FROM customers; 
# - Whenever you would like to refer to an SQL object in your queries, you must specify the databse to which it is applied.
# SQL objets: SQL Table, views, stored procedures, functions

# 1 ) set a default database eg: USE Sales;
# 2 ) call a table from a certain database
