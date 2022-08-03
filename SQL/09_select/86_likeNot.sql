# 86 : LIKE - NOT LIKE

SELECT * FROM employees
WHERE first_name LIKE('MAR%');

SELECT * FROM employees
WHERE first_name LIKE('%AR');

SELECT * FROM employees
WHERE first_name LIKE('%AR%');

SELECT * FROM employees
WHERE first_name LIKE('MAR_');

SELECT * FROM employees
WHERE first_name NOT LIKE('MAR_');

# 87 : Exercise
SELECT * FROM employees
WHERE first_name LIKE ('MARK%');

SELECT * FROM employees
WHERE hire_date LIKE ('%2000%');

SELECT * FROM employees
WHERE emp_no LIKE ('1000_');














