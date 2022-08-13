# 156 : ROUND()

# ROUND(#, decimal_places)
#	- numberic, or math, fxn you can use
#	- usually applied to the single values that aggregate fxns return.

select avg(salary) from salaries;
select round(avg(salary),2) from salaries;

# --- 157 exercise ---
select * from salaries;
select round(avg(salary),2) from salaries where from_date > '1997-01-01';