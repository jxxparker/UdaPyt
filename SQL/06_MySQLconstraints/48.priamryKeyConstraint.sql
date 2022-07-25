#Foreign Key Contraint
# - a foreign key in sql is defined through a foreign constraint
# - the foreign key maintains the referential integrity within the database

CREATE TABLE sales
(
	purchase_number INT AUTO_INCREMENT,
	date_of_purchase DATE,
	customer_id INT,
    item_code VARCHAR(10),
PRIMARY KEY (purchase_number),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id) on DELETE CASCADE
);

 



