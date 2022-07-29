# 47 : PRIMARY KEY Constraint - exercise
# Drop the "customers" table and re-create it using the following code:
CREATE TABLE customers                                                              
(  
	customer_id INT,  
    first_name varchar(255),  
    last_name varchar(255),  
    email_address varchar(255),  
    number_of_complaints int,  
primary key (customer_id)  
);

# Then, create the "items" table
-- (columns - data types:  
-- item_code – VARCHAR of 255,  
-- item – VARCHAR of 255,  
-- unit_price – NUMERIC of 10 and 2,  
-- company­_id – VARCHAR of 255),  
-- and the “companies” table  
-- company_name – VARCHAR of 255,  
-- headquarters_phone_number – integer of 12). 

CREATE TABLE items
( 
	item_code VARCHAR(255),
    item VARCHAR(255),
    unit_price numeric(10,2),
    company_id VARCHAR(255),
primary key(item_code)
);

CREATE TABLE companies
(
	company_id VARCHAR(255),
    company_name VARCHAR(255),
    headquarters_phone_number INT(12),
primary key(company_id)
);



