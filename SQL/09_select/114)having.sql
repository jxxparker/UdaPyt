# 114 : HAVING
# - refines the output from records that do not satisfy a certain condtion
# - frequently implemented with GROUP BY
# - after HAVING, you can have a condition with an aggregate function,
#	while WHERE cannot use aggregate fxns within its conditions

SELECT * FROM employees
HAVING hire_date >= '2000-01-01';

SELECT first_name, COUNT(first_name) AS names_count
FROM employees 
GROUP BY first_name
HAVING COUNT(first_name) > 250
ORDER BY first_name;

# ORDER : COUNT() -> aggregate fxn -> HAVING
# 115 : Exercise

SELECT emp_no, AVG(salary)
FROM salaries
GROUP BY emp_no
HAVING AVG(salary) > 120000
ORDER BY emp_no;










