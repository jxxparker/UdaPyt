# 188 : CROSS JOIN

# a cross join will take the values from a certain table and
# connecting them with all the values from the tables we want to join it with

# inner join : typically connects only the matching values

# CROSS JOIN : 
#	- connects all the values, not just those that match
#	- the Cartesian product of the values of two or more sets
#	- particualrly useful when the tables in a database are not well connected

use employees;

select dm.*, d.* 
from dept_manager dm
cross join departments d
order by dm.emp_no, d.dept_no;


select dm.*, d.*
from dept_manager dm, departments d
order by dm.emp_no, d.dept_no;


select dm.*, d.*
from dept_manager dm
join departments d 
order by dm.emp_no, d.dept_no;


select dm.*, d.*
from departments d 
cross join dept_manager dm
where d.dept_no <> dm.dept_no
order by dm.emp_no, d.dept_no;


# 189 : Exercise
select * from dept_manager;

select dm.*, d.*
from departments d 
cross join dept_manager dm
where d.dept_no = 'd009' order by d.dept_no;


# 191 : Exercise
SELECT e.*, d.*
FROM employees e
CROSS JOIN departments d
WHERE e.emp_no < 10011
ORDER BY e.emp_no, d.dept_name;













