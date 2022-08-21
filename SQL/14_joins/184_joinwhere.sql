# 184 : JOIN and WHERE used together
 
# Join : used for connecting the "Employees" and "Salaries" tables
# WHERE : used to define the condition or conditions that will determine which will be
#			the connecting points between the two tables

-- select e.emp_no, e.first_name, e.last_name, s.salary
-- from employees e
-- join salaries s on e.emp_no = s.emp_no
-- where s.salary > 145000;


# 186 : Exercise
select * from employees;
select * from titles;

select e.first_name, e.last_name, e.hire_date, t.title, e.emp_no
from employees e
join titles t on e.emp_no = t.emp_no
where e.first_name = 'Margareta' and e.last_name = 'Markovitch'
order by e.emp_no;












