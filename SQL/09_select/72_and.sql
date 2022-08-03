# 72 : AND

# = equal operator
# in SQL, there are many other linking keybwoards, and symbols, called operators, that you can use with the 
# WHERE clause

# AND, OR, IN, LIKE, BETWEEN
# AND : allows you to logically combine two statements in the condition code block

SELECT * FROM employees
WHERE first_name = 'Parto' AND gender = 'M';

# 73 : Exercise
SELECT * FROM employees
WHERE first_name = 'Kellie' AND gender = 'F';
