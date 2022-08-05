# 124 : The INSERT statement
use employees;
SELECT * FROM employees ORDER BY emp_no DESC LIMIT 10;
-- INSERT INTO employees (
-- emp_no,
-- birth_date,
-- first_name,
-- last_name,
-- gender,
-- hire_date ) VALUES (
-- 999901, '1986-04-21', 'John', 'Smith', 'M', '2011-01-01');
 
# 125 : Part 2
INSERT INTO employees (
birth_date,
emp_no,
first_name,
last_name,
gender,
hire_date ) VALUES (
'1973-3-26', 999902, 'Patricia', 'Lawrence', 'F', '2005-01-01');

# 126 : Exercise
use employees;
SELECT * FROM titles
WHERE emp_no = 999903;
INSERT INTO titles
(emp_no, title, from_date) 
VALUES (500000, 'Senior Engineer', '1997-10-01');




















