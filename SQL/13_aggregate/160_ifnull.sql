# 160 : IFNULL() AND COALESCE()

# ifnull(expression1, expression2)
#	- returns the first of the two indicated values if the data value found in the
#		the table is not null, and returns the second value if there is a null value
#	- prints the returned value in the column of the output
#	- COALESCE() will always return a single value of the ones we have
#		within parentheses, and this value will be the first non-null value of 
#		this list, reading the values from left to right. 
#	- if COALESCE() has two arguments, it will work preciesely like IFNULL()

use employees;
select * from departments_dup order by dept_no;

select dept_no, IFNULL(
dept_name, 'Department name not provided') as dept_name
from departments_dup;

select dept_no, COALESCE(
dept_name, 'Department name not provided') as dept_name
from departments_dup;

select * from departments_dup order by dept_no;

select dept_no, dept_name, 
coalesce(dept_manager, dept_name,'N/A')
from departments_dup order by dept_no asc;

# 161 : another example of coalesce
SELECT dept_no, dept_name,
COALESCE('department manager name') as fake_col
from departments_dup;


# 162 exercise 
select * from departments_dup;
select dept_no, dept_name,
coalesce(dept_no, dept_name) as dept_info
from departments_dup order by dept_no asc;


SELECT
IFNULL(dept_no, 'N/A') as dept_no,
IFNULL(dept_name,
'Department name not provided') AS dept_name,
COALESCE(dept_no, dept_name) AS dept_info
FROM departments_dup
ORDER BY dept_no ASC;













