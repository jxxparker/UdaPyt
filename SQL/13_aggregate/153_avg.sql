# 153 : AVG()

# AVG() : extracts the average value of all non-null values in a field

select min(salary) from salaries;

select avg(salary) from salaries;

# --- 154 exercise ---

select * from salaries;
select avg(salary) from salaries where from_date > '1997-01-01';