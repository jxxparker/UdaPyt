# Creating a Table

# CREATE DATABASE [IF NOT EXISTS] sales;
# CREATE TABLE "table_name" ();
# compulsory requirement : add at least one column
# AUTO_INCREMENT : frees you from having to insert all purchase numbers manually through the INSERT command at a later stage.
#	- assigns 1 to the first record of the table and automatically increments by 1 for every subsequent row.

CREATE TABLE sales 
( 
	purchase_number INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    date_of_purchase DATE NOT NULL, 
    customer_id INT,
    item_code VARCHAR(10) NOT NULL
); 