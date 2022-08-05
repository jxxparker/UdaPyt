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
if [ -f $FILE ]; then

    #default variables
    VAR_READ="NO"
    VAR_WRITE="NO"
    VAR_EXT=""

    #CHECK IF FILE IS READABLE
    if [ -r $FILE ]; then
        VAR_READ="YES"
    fi

    # check if file is writable
    if [ -w $FILE ]; then
        VAR_WRITE="YES"
    fi

    # check if file is executable
    if [ -x $FILE ]; then
        VAR_EXE="YES"
    fi

    #write permission summary to user
    echo "READ: $VAR_READ"













