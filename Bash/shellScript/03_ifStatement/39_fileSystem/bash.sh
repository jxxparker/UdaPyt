#!/bin/bash

# for provided file print the summary of what permissions user has granted
# example: ./filetest.sh hello.txt
# READ : YES
# WRITE : NO
# EXECUTE : NO

# ARGUMENT CHECK
if [ $# -ne 1 ]; then
    echo "provide exactly one argument"
    exit 1
fi

#variable assignment
FILE=$1

# check if the file exists
if [[ -f $FILE ]]; then
    # default variables
    VAR_READ="NO"
    VAR_WRITE="NO"
    VAR_EXE="NO"

    # check if file is readable
    if [[ -r $FILE ]]; then
        VAR_READ="YES"
    fi

    # check if file is writable
    if [[ -w $FILE ]]; then
        VAR_WRITE="YES"
    fi

    # check if file is executeable 
    if [[ -x $FILE ]]; then
        VAR_EXE="YES"
    fi

    # write permission summary to user
    echo "=== FILE : $FILE ==="
    echo "READ :    $VAR_READ"
    echo "WRITE :   $VAR_WRITE"
    echo "EXE :     $VAR_EXE"

else
    if [[ -d $FILE ]]; then
        echo $FILE is a directory
    else  
        echo FILE : $FILE does not exists
    fi
fi
















