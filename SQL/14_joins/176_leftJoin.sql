# 176 : LEFT JOIN

# left join
select m.dept_no, m.emp_no, d.dept_name
from dept_manager_dup m
left join departments_dup d on m.dept_no = d.dept_no
group by m.emp_no order by m.dept_no;


# 177 : part 2

select * from departments_dup;  #dept_no, dept_name
select * from dept_manager_dup; #emp_no, dept_no, from_date, to_date

select m.dept_no, m.emp_no, d.dept_name
from departments_dup d
left join dept_manager_dup m on m.dept_no = d.dept_no
group by m.emp_no order by m.dept_no;


select d.dept_no, m.emp_no, d.dept_name
from departments_dup d
left outer join dept_manager_dup m on m.dept_no = d.dept_no
order by d.dept_no;


# 178 : Exercise
select * from employees; #emp_no, birth, first, last, gender, hire
select * from dept_manager; #emp_no, dept_no, from_date, to_date

select e.emp_no, e.first_name, e.last_name, dm.dept_no, dm.from_date
from employees e
left join dept_manager dm on e.emp_no = dm.emp_no
where e.last_name = 'Markovitch'
order by dm.dept_no desc, e.emp_no;




























