# 117 : WHERE vs HAVING 

# WHERE : allows us to set conditions that refer to subsets of individual rows
SELECT first_name, count(first_name) as names_count
FROM employees
WHERE hire_date > '1990-01-01'
group by first_name
HAVING count(first_name) < 200
order by first_name ASC;

# 118 : WHERE vs HAVING p2
# 119 : Exercise
SELECT * FROM dept_emp ORDER BY emp_no;
SELECT emp_no FROM dept_emp
WHERE from_date > '2000-01-01' 
GROUP BY emp_no HAVING COUNT(from_date) > 1
ORDER BY emp_no;
















