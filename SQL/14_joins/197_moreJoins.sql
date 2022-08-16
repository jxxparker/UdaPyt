# 197 : Tips and Tricks for joins

# JOINS : one should look for key columns, which are common between the tables involved
#			in the analysis and are necessary to solve the task at hand
#	- these columns do not need to be foreign or private keys


SELECT d.dept_name, AVG(salary) as average_salary
FROM departments d
JOIN dept_manager m ON d.dept_no = m.dept_no
JOIN salaries s ON m.emp_no = s.emp_no
group by d.dept_no
order by d.dept_no;
    
    
# 198 : exercise
select * from employees; #emp_no
select * from dept_manager; #emp_no

select e.gender, COUNT(dm.emp_no)
from employees e
join dept_manager dm on e.emp_no = dm.emp_no
group by gender;












    
