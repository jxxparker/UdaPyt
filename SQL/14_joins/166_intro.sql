# 166 : Introductions to JOINS

# joins : the SQL tool that allow us to construct a relationship between objects

# 167 : Exercise
use employees;

ALTER TABLE departments_dup

CHANGE COLUMN dept_no dept_no CHAR(4) NULL;

ALTER TABLE departments_dup

CHANGE COLUMN dept_name dept_name VARCHAR(40) NULL;

INSERT INTO departments_dup(dept_no) VALUES ('d010'), ('d011');


INSERT INTO dept_manager_dup

select * from dept_manager;

