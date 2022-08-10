# 139 : Delete Statement

use employees;
commit;

select * from employees where emp_no = 999901;
select * from titles where emp_no = 10671;

DELETE FROM employees where emp_no = 999901;

rollback;

# on delete cascade
#	- if a specific value from the parent table's primary key has been deleted, all the record
#		from the child table referring to this value will be removed as well
