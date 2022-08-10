# 134: Update Statement

# the Update Statement 
#	- used to update the values of existing records in a table
use employees;

select * from employees where emp_no=999901;

update employees set
	first_name = 'Stella',
    last_name = 'Parkinson',
    birth_date = '1990-12-31',
    gender = 'F'
where emp_no = 999901;

select * from employees order by emp_no desc limit 10;