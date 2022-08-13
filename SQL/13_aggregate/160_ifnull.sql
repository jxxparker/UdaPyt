# 160 : IFNULL() AND COALESCE()

# ifnull(expression1, expression2)
#	- returns the first of the two indicated values if the data value found in the
#		the table is not null, and returns the second value if there is a null value
#	- prints the returned value in the column of the output
#	- COALESCE() will always return a single value of the ones we have
#		within parentheses, and this value will be the first non-null value of 
#		this list, reading the values from left to right. 
#	- if COALESCE() has two arguments, it will work preciesely like IFNULL()

select * from departments_dup order by dept_no;

select dept_no, IFNULL(
dept_name, 'Department name not provided') as dept_name
from departments_dup;

select dept_no, COALESCE(
dept_name, 'Department name not provided') as dept_name
from departments_dup;








