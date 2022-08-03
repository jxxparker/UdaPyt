# 104 : Intro to Aggregate Fxns

# Aggregate Fxns : they are applied on multiple rows of a single column of a table and
#					return an output of a single value

# COUNT() : counts the number of non-null records in a field
# SUM() : sums all the non-null values in a column
# MIN() : returns the minimum value from the entire list
# MAX() : returns the maximum value from the entire list
# AVG() : calculates the avg of all non null values belonging to a certain column of a table

SELECT * FROM employees;

SELECT COUNT(emp_no) from employees;
SELECT COUNT(first_name) from employees;
SELECT COUNT(DISTINCT first_name) from employees;

# 105 : Exercise
SELECT * from salaries;
SELECT COUNT(*) from salaries
WHERE salary >= 100000;

SELECT * FROM dept_manager;
SELECT COUNT(*) FROM dept_manager;


















