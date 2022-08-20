# 214 : Self Join

use employees;

# self join 
#	- applied when a table must join itself
# 	- if you'd like to combine certain rows of a table with other rows of the
#	- same table, you need a self-join

select * from emp_manager order by emp_manager.emp_no;

select e1.*
from emp_manager e1 
join emp_manager e2 ON e1.emp_no = e2.manager_no
where e2.emp_no IN (SELECT
manager_no from emp_manager);