3.31 : String Comparison

- Compare two strings
    : [ "$STR1" = "$STR2" ]
    : [ "$STR1" != "$STR2" ]
    : [ "$STR1" = "hello" ]
    : [ "$STR1" != "hello" ]
    : [ "$STR1" = "$STR2" ]

If STR1 or STR2 are not defined or empty, we would get error message: 
Unary operator expected when not using " " quotation marks

- Bash can handle it in another way [[]]

- Test if string is empty
    - [ -z "$STR1" ] : returns true if STR1 holds an empty string
    - [[ -z "$STR1" ]] : similar to above, but not widely used

    - [ -n "$STR1" ] : returns true if STR1 holds a non-empty string


- Alphabetically compare two strings
    - If you want to compare alphabetically, you must use double brackets. 
    - [[ $STR1 > $STR2 ]]
    - [[ $STR1 < $STR2 ]]


- Wildcards
    - [[ $STR1 == string-with-wildcards ]]

- Regular expressions
    - [[ $STR1 =~ $regex ]]