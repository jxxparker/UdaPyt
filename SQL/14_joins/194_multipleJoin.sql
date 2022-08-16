# 194 : JOIN more than two tables in SQL

# when creating a query that joins multiple tables, you must back it with
# strong intuition and a crystal-clear idea of how you would lke the tables to be connected

select e.first_name, e.last_name, e.hire_date, m.from_date, d.dept_name
from employees e
join dept_manager m on e.emp_no = m.emp_no
join departments d on m.dept_no = d.dept_no;


select e.first_name, e.last_name, e.hire_date, m.from_date, d.dept_name
from departments d
join dept_manager m on d.dept_no = m.dept_no
join employees e on m.emp_no = e.emp_no;

select e.first_name, e.last_name, e.hire_date, m.from_date, d.dept_name
from departments d
JOIN dept_manager m on d.dept_no = m.dept_no
RIGHT JOIN employees e on m.emp_no = e.emp_no;


# 195 : Exercise
select * from employees;
select * from dept_emp;
select * from departments;

SELECT e.first_name, e.last_name, e.hire_date, t.title, m.from_date, d.dept_name
FROM employees e
JOIN dept_manager m ON e.emp_no = m.emp_no
JOIN departments d ON m.dept_no = d.dept_no
JOIN titles t ON e.emp_no = t.emp_no
WHERE t.title = 'Manager'
ORDER BY e.emp_no;










