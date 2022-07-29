# Primary Key Constraint

# Constraints : specific rules, or limits, that we define in our tables.
# 				- the role of contraints is to outline the existing relationships between different 	
#					tables in our database
# e.g : NOT NULL

CREATE TABLE sales
(
	purchase_number INT AUTO_INCREMENT,
    date_of_purchase DATE,
    customer_id INT,
    item_code VARCHAR(10),
PRIMARY KEY (purchase_number)
);