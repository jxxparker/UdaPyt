# 89 : Wild Character


# Wild characters : %, _, *
# % : LIKE ('MAR%') : a substitute for a sequence of characters
# _ : LIKE('MAR_') : helps you match a single character
# * : SELECT * FROM employees; will deliver a list of all columns in a table

# Exercise
SELECT * FROM employees
WHERE first_name LIKE ('%JACK%');

SELECT * FROM employees
WHERE first_name NOT LIKE ('%JACK%');





