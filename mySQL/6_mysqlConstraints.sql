-- CREATE TABLE sales
-- (
-- 	purchase_number INT AUTO_INCREMENT,
--     date_of_purchase DATE,
--     customer_id INT,
--     item_code VARCHAR(10),
-- primary key (purchase_number)
-- -- foreign key (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
-- );  

-- DROP TABLE sales;


-- ALTER TABLE sales
-- ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE;

-- ALTER TABLE sales
-- DROP FOREIGN KEY sales_ibfk_1;

DROP TABLE sales;

DROP TABLE customers;

DROP TABLE items;

DROP TABLE companies;