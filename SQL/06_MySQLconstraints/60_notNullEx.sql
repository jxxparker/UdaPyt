# 59 : Not null Constraint p1 exercise

# Using ALTER TABLE, first add the NULL constraint to the 
# headquarters_phone_number field in the “companies” table, and then drop that same constraint.

ALTER TABLE companies
MODIFY headquarters_phone_number VARCHAR(255) NULL;

