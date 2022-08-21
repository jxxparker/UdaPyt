# 175 : Duplicate Records

use employees;
INSERT INTO dept_manager_dup
VALUES ('110228', 'd003', '1992-03-21', '9999-01-01');

INSERT INTO departments_dup
VALUES ('d009', 'Customer Service');

# check 'dept_manager_dup' and 'departments_dup'

select * from dept_manager_dup #emp_no, dept_no, from_date, to_date
order by dept_no asc;

select * from departments_dup #dept_no, dept_name
order by dept_no asc;

# inner join

select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m 
join departments_dup d on m.dept_no = d.dept_no
GROUP BY m.emp_no
order by dept_no;



















