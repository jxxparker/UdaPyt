# 206 : SQL Subqueries with EXISTS-NOTEXISTS Nested inside where

# EXISTS : checks whether cetain row values are found within a subquery
#	- this check is conducted row by row
#	- it returns a Boolean value

# if a row value of subquery exists -> TRUE -> the corresponding record the other query is extracted
# if a row value of subquery doesnt exists -> False -> no row value from the outer query is extracted

use employees;

select e.first_name, e.last_name
from employees e
where exists 
(SELECT * FROM dept_manager dm where dm.emp_no = e.emp_no) 
order by emp_no;


# 207 : Exercise
select * from employees; #emp_no
select * from titles;

select * from employees e
where exists
( select * from titles t where title = "Assistant Engineer")
order by emp_no;










