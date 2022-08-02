# 55 : Default Constraint

# Default Constraing : helps us assign a particular default value to every row of a column.
#	- a value different from the default can be stored in a field where the 
#		DEFAULT constraint has been applied, only if specifically indicated

CREATE TABLE customers (
customer_id INT,
first_name VARCHAR(255),
last_name VARCHAR(255),
email_address VARCHAR(255),
number_of_complaints INT, 
PRIMARY KEY (customer_id)
);

ALTER TABLE customers 
CHANGE COLUMN number_of_complaints number_of_complaints INT DEFAULT 0;

INSERT INTO customers (first_name, last_name, gender)
VALUES ('PETER', 'FIGARO', 'M');

SELECT * FROM customers;
ALTER TABLE customers
ALTER COLUMN number_of_complaints DROP DEFAULT;




