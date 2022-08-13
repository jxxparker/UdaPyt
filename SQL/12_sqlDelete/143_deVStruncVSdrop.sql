# 143 : drop vs truncate vs delete

# Drop : you won't be able to roll back to its initial state, or to the last COMMIT statement
# - use DROP table only when you are sure you arne't going to use the table in question anymore

# Truncate : when truncating, auto-increment values will be reset

# Delete : removes records row by row

# Truncate vs delete withtout WHERE
#	: the sql optimizer will implement different programmtic approaches when we are using TRUNCATE or DELETE
#	: auto - increment values are not reset with delete
