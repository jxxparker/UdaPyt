# 130 : Inserting data into a new table

SELECT * FROM departments LIMIT 10;

CREATE TABLE departments_dup
(
dept_no CHAR(4) NOT NULL,
dept_name VARCHAR(40) NOT NULL
);
SELECT * FROM departments_dup;

INSERT INTO departments_dup (
dept_no, dept_name)
SELECT * FROM departments;

# 131 : Exercise

INSERT INTO departments VALUES ('d010', 'Business Analysis');

SELECT * FROM departments;


