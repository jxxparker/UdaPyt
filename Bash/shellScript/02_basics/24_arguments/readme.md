2.24 : Arguments

- Passing arguments into script
- Passing arguments into function
- Example of calling a script with three arguments:
    ./arguments one two three


$0 - script name
$1 - first argument
$2 - second argument
$n - nth argument
"$@" - all arguments, expands as "$1" "$2" "$3" and so on
"$*" - all arguments, expands as one string "$1c$2c$3", where c is the 
        first character of IFS (internal field separator)
        First character of IFS is usually space.
$# - arguments count