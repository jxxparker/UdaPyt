# 140 : The Delete Statement 2

select * from departments_dup order by dept_no;
commit;
-- delete from departments_dup;
rollback;

# 141 : exercise
select * from departments;
delete from departments where dept_no = 'd010';
rollback;