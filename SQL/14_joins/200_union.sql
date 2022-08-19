# 200 : Union vs Union ALL

# Union All
#	- used to combine a few select statements in a single output
#	- you can think of it as a tool that allows you to unify tables

# create employees_dup

DROP TABLE IF EXISTS employees_dup;

CREATE TABLE employees_dup (
emp_no int(11),
birth_date date,
first_name varchar(14),
last_name varchar(16),
gender enum('M', 'F'),
hire_date date
);

insert into employees_dup
select e.* 
from employees e
limit 20;

select * from employees_dup;

insert into employees_dup values
('10001', '1953-09-02', 'Georgi', 'Facello', 'M', '1986-06-26');


select e.emp_no, e.first_name, e.last_name, NULL AS dept_no, NULL AS from_date
FROM employees_dup e
where e.emp_no = '10001'
union all select
null as emp_no, null as first_name, null as last_name, m.dept_no, m.from_date
from dept_manager m;


# 201 : Exercise

SELECT * FROM
(
SELECT e.emp_no, e.first_name, e.last_name, NULL AS dept_no, NULL AS from_date
FROM employees e
WHERE last_name = 'Denis' UNION SELECT
NULL AS emp_no, NULL AS first_name, NULL AS last_name, dm.dept_no, dm.from_date
FROM dept_manager dm) as a ORDER BY -a.emp_no DESC;























