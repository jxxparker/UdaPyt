# 203 : SQL Subqueries with iN nested inside WHERE

use employees;

# subqueries = inner queries = nested queries
#	- queries embedded in a query
#	- they are part of another query, called an OUTER QUERY

select * from dept_manager;

#select the first and last name from the "Employees" table for the same
#employee nubmers that can be foudn in the "Department Manager" table

select e.first_name, e.last_name
from employees e
where e.emp_no IN 
( SELECT dm.emp_no from dept_manager dm);

SELECT dm.emp_no 
from dept_manager dm;


# 204 : Exercise
select * from dept_manager; # emp_no, dept_no, from_date, to_date
select * from employees; #emp_no, birth_date, first, last, gender, hire_date

select * from dept_manager
where emp_no IN 
( SELECT emp_no from employees where hire_date between '1990-01-01' AND '1995-01-01');











