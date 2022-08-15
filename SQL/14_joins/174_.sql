# 174 : A note on using joins
select * from dept_manager_dup;

select m.dept_no, m.emp_no, m.from_date, m.to_date, d.dept_name
from 
dept_manager_dup m
inner join
departments_dup d on m.dept_no = d.dept_no
order by m.dept_no;


-- select m.dept_no, m.emp_no, d.dept_name
-- from dept_manager_dup m
-- inner join 
-- departments_dup d ON m.dept_no = d.dept_no;