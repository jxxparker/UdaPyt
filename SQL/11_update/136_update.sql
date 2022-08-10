# 136 : The update statement p2

# the update statement
#	- used to update the values of existing records in a table
 
select * from departments_dup order by dept_no;
SET SQL_SAFE_UPDATES=0;

update departments_dup set
	dept_no = 'd011',
    dept_name = 'Quality Control';
COMMIT;
rollback;

# 137 : Exercise
select * from departments;
update departments set dept_name = "Data de" where dept_no = "d010";
rollback;

