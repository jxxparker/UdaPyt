# 147 : SUM()

select * from salaries;

select sum(salary) from salaries;

-- select sum(*) from salaries; error

# --- 148 exercise ---
select * from salaries;
select sum(salary) from salaries where from_date > '1997-01-01';