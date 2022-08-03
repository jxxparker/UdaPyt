# 81 : NOT IN

SELECT * FROM employees
WHERE first_name NOT IN ('Cathie', 'Mark', 'Nathan');

SELECT * FROM employees
WHERE first_name IN ('Cathie', 'Mark', 'Nathan');

# 82 : IN Exercise 
SELECT * FROM employees
WHERE first_name IN ('Dennis', 'Elvis');

# 84 : NOT IN Exercise
SELECT * FROM employees
WHERE first_name NOT IN ('Mark', 'John', 'Jacob');