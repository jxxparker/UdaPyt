# 176 : LEFT JOIN

DELETE from dept_manager_dup
where emp_no = '110228';

delete from departments_dup
where dept_no = 'd009';

# add back the initial records
INSERT into dept_manager
values ('110228', 'd003', '1992-03-21', '9999-01-01');

insert into departments_dup
values ('d009', 'Customer Service');

# left join
select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
left join 
departments_dup d on m.dept_no = d.dept_no
group by m.emp_no order by m.dept_no;


# 177 : part 2

select m.dept_no, m.emp_no, d.dept_name
from departments_dup d
left join 
dept_manager_dup m on m.dept_no = d.dept_no
group by m.emp_no order by m.dept_no;


select d.dept_no, m.emp_no, d.dept_name
from departments_dup d
left join 
dept_manager_dup m on m.dept_no = d.dept_no
order by d.dept_no;


# 178 : Exercise
select * from employees;
select * from dept_manager;

select d.emp_no, d.birth_date, d.first_name, d.last_name, m.dept_no, m.from_date
from employees d
left join 
dept_manager m on d.emp_no = m.emp_no
where d.last_name = 'Markovitch'
order by m.dept_no desc, d.emp_no;



























