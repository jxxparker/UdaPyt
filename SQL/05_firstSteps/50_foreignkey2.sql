# 50 : Foreign Key Constraint p2
USE sales;
DROP TABLE sales;
CREATE TABLE sales
(
	purchase_number INT AUTO_INCREMENT,
    date_of_purchase DATE,
    customer_id INT,
    item_code VARCHAR(10),
PRIMARY KEY (purchase_number),
FOREIGN KEY(customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE
);

-- ALTER TABLE sales
-- ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE;

ALTER TABLE sales
DROP FOREIGN KEY sales_ibfk_1;