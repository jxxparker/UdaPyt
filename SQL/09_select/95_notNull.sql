# 95 : IS NOT NULL/ IS NULL

# IS NOT NULL : used to extract value that are not null
SELECT * FROM employees
WHERE first_name IS NOT NULL;

SELECT * FROM employees
WHERE first_name IS NULL;

# 96 : Exercise
SELECT * FROM departments
WHERE dept_no IS NOT NULL;


