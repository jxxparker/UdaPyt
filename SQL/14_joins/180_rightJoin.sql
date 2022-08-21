# 180 : Right Join

select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
right join departments_dup d on m.dept_no = d.dept_no
order by dept_no;


select m.dept_no, m.emp_no, d.dept_name
from departments_dup d
left join dept_manager_dup m on m.dept_no = d.dept_no
order by dept_no;
