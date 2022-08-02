# 49 : Foreign Key Constraint

# foreign key : points to a column of another table and, thus, links the two tables.
# a foreign key in sql is defined through a foreign key constraint.
# 	- the foreign key maintains the referential integrity within the database.

CREATE TABLE sales
(
	purchase_number INT AUTO_INCREMENT,
    date_of_purchase DATE,
    customer_id INT,
    item_code VARCHAR(10),
PRIMARY KEY (purchase_number),
FOREIGN KEY(customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE
);

# ON DELETE CASCADE :
# 	- if a specific value from the parent table's primary key has been deleted, all the records
#	- from the child table referring to this value will be removed as well.
