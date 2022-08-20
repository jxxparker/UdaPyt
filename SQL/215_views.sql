# 215 : Views

# Using SQL views
# SQL View : a virtual table whose contents are obtained from an existing table
#				or tables, called base tables

# SQL View 
#	- think of a view object as a view into the base table
#	- the view itself does not contain any real data; the data is physically stored in the base table
#	- the view simply shows the data contained in the base table

use employees;
select * from dept_emp;

select emp_no, from_date, to_date, COUNT(emp_no) AS Num
from dept_emp 
GROUP BY emp_no having Num > 1;


SELECT emp_no, MAX(from_date) as from_date, MAX(to_date) AS to_date
FROM dept_emp
GROUP BY emp_no;


# 215 : Exercise

select * from salaries;

CREATE OR REPLACE VIEW v_manager_avg_salary AS
SELECT ROUND(AVG(salary), 2)
FROM salaries s
JOIN dept_manager m ON s.emp_no = m.emp_no;










