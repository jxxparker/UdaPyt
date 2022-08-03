# 110 : Group By

# - When working in SQL, results can be grouped according to a specific field or fields
# Group By : must be placed immediately after the WHERE conditions, if any, and just before
# 			the ORDER BY clause

SELECT first_name FROM employees
GROUP BY first_name;

SELECT DISTINCT first_name FROM employees;

SELECT first_name, count(first_name) 
FROM employees GROUP BY first_name
ORDER BY first_name DESC;