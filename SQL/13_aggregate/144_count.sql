# 144 : Count

# aggregate functions 
#	: they gather data from many rows of a table, then aggregate it into a single value
#	: input ( the info contained in multiple rows ) -> output ( the single value they provide )
# 	: ex - count(), sum, min, max, avg
#	: count(distinct) - helps us find the number of times unique values are encountered in a given column
#	count() - aggregate fxn typically ignore null values throughout the field to which they are applied.

use employees;
select * from salaries order by salary desc limit 10;

select count(salary) from salaries;

select count(distinct from_date) from salaries;

select count(*) from salaries;

# --- 145 : exercise ---
select * from dept_emp;
select count(distinct dept_no) from dept_emp;
















