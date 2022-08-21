# 174 : A note on using joins
select * from dept_manager_dup;

select m.dept_no, m.emp_no, m.from_date, m.to_date, d.dept_name
from dept_manager_dup m
inner join departments_dup d on m.dept_no = d.dept_no
order by m.dept_no;

-- select m.dept_no, m.emp_no, d.dept_name
-- from dept_manager_dup m
-- inner join 
-- departments_dup d ON m.dept_no = d.dept_no;


select * from employees; # emp_no, birth, first, last, gender, hire_date
select * from emp_manager; #emp_no, dept_no, manager_no
select * from dept_manager; #emp_no, dept_no, from_date, to_date


SELECT m.dept_no, m.emp_no, d.dept_name
FROM dept_manager_dup m
inner join departments_dup d on m.dept_no = d.dept_no
order by d.dept_no;

#inner join = join


















