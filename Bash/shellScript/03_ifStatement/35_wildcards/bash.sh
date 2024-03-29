#!/bin/bash

# backup all .pdf files from prod location : 
# /Users/jihunpark/UdaPyt/Bash/shellScript/03_ifStatement/35_wildcards
# Script takes one argument :
# destination path - which needs to ends with /backup e.g
# /Users/jihunpark/UdaPyt/Bash/shellScript/03_ifStatement/35_wildcards

PROD=/Users/jihunpark/UdaPyt/Bash/shellScript/03_ifStatement/35_wildcards
# arguments check
if [[ $# -ne 1 ]]; then
    echo "Only one argument is needed, run $0 destination-path"
    exit 1
fi

# destination path check
DESTINATION=$1
if [[ $DESTINATION != */backup ]]; then
    echo Wrong destination path, destination path must ends with /backup
    exit 2
fi

# create destination folder
DATE=$(date +%Y-%m-%d_%H_%M_%S)
mkdir -p $DESTINATION/$DATE

# copy from prod to destination 
cp $PROD/*.pdf $DESTINATION/$DATE

# test exit status of copy command
if [[ $? -eq 1 ]]; then   
    echo backup OK
else
    echo backup failed
fi


