# 181 : The new and old join of syntax

# -- JOIN
select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
inner joindepartments_dup d on m.dept_no = d.dept_no
order by m.dept_no;


# -- WHERE
select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m, departments_dup d
where m.dept_no = d.dept_no
order by m.dept_no;


# 182 : Exercise
select * from dept_manager;
select * from employees;

select e.emp_no, e.first_name, e.last_name, dm.dept_no, e.hire_date
from employees e
join dept_manager dm on e.emp_no = dm.emp_no;























