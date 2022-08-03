# 92 : Between - AND

# BETWEEN... AND...
# - helps us designate the interval to which a given value belongs

SELECT * FROM employees
WHERE hire_date BETWEEN '1990-01-01' AND '2001-01-01';

# NOT BETWEEN AND
# - will refer to an interval composed of two parts:

SELECT * FROM employees
WHERE hire_date NOT BETWEEN '1990-01-01' AND '2000-01-01';

# 93 : Exercise
SELECT * FROM salaries
WHERE salary BETWEEN '66000' AND '70000';

SELECT * FROM salaries
WHERE emp_no NOT BETWEEN '10004' AND '10012';

SELECT * FROM departments
WHERE dept_no BETWEEN 'd003' AND 'd006';


















