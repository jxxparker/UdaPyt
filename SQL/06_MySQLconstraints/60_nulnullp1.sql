# 58 : Not null constraint

# the "not null" restriction is applied through the NOT NULL Constraint
# when you insert values in the table, you cannot leave the respective field empty
# if you leave it empty, MySql will signal an error

CREATE TABLE companies (
company_id iNT AUTO_INCREMENT,
headquarters_phone_number VARCHAR(255),
company_name VARCHAR(255) NOT NULL,
PRIMARY KEY (company_id)
);

ALTER TABLE companies
MODIFY company_name VARCHAR(255) NULL;

ALTER TABLE companies
CHANGE COLUMN company_name company_name VARCHAR(255) NOT NULL;

INSERT INTO companies (headquarters_phone_number)
VALUES ('+1 (202) 555-0196')
;

SELECT * FROM companies;