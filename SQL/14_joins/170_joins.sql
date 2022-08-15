# 170 : Inner Join
use employees;
# Inner Join : can help us extract this result set

SELECT * from dept_manager_dup order by dept_no;
select * from departments_dup order by dept_no;

# 171 : Inner Join

select *from dept_manager_dup;
select * from departments_dup;

select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
inner join
departments_dup d on m.dept_no = d.dept_no 
order by m.dept_no;

# 172 : Exercise












