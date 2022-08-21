# 170 : Inner Join
use employees;
# Inner Join : can help us extract this result set

SELECT * from dept_manager_dup order by dept_no;
select * from departments_dup order by dept_no;

# 171 : Inner Join

select * from dept_manager_dup; #emp_no, *dept_no, from_date, to_date
select * from departments_dup; #*dept_no, dept_name

select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
inner join
departments_dup d on m.dept_no = d.dept_no 
order by m.dept_no;

# 172 : Exercise

select * from employees; # emp_no, birth, first, last, gender, hire_date
select * from emp_manager; #emp_no, dept_no, manager_no
select * from dept_manager; #emp_no, dept_no, from_date, to_date

select e.first_name, e.last_name, e.hire_date, e.emp_no, em.dept_no
from employees e
join
emp_manager em on e.emp_no = em.emp_no;
















