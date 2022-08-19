# 209 : Subqueries nested in select and from

select emp_no from dept_manager
where emp_no = 110022;

# assign employee number 110022 as a manager to all employees from 10001 to 10020, and employee number
# 110039 as a manager to all employees from 10020 to 10040.


SELECT e.emp_no AS employee_ID, 
MIN(de.dept_no) AS department_code,
(SELECT emp_no FROM dept_manager
WHERE emp_no = '110022') AS manager_ID
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
WHERE e.emp_no <= 10020
GROUP BY e.emp_no
ORDER BY e.emp_no;



SELECT A.* FROM 
(SELECT e.emp_no AS employee_ID,
MIN(de.dept_no) AS department_code,
(SELECT emp_no FROM dept_manager
WHERE emp_no = 110022) AS manager_ID
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
WHERE e.emp_no <= 10020
GROUP BY e.emp_no
ORDER BY e.emp_no) AS A;


# 210 : Exercise












