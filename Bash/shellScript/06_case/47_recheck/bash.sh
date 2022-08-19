#!/bin/bash

# read data from users and make them option to recheck if provided data are correct

echo -n "Enter your name : "
read NAME
echo -n "Enter your age : "
read AGE
echo -n "Enter your department : "
read DEPARTMENT

echo "You have entered following : "
echo "NAME :            $NAME"
echo "AGE :             $AGE"
echo "DEPARTMENT :      $DEPARTMENT"


CHECK=0
while [ $CHECK -eq 0 ]
do 

echo -n "Is that correct? [Y/n] "
read ANSWER

case "$ANSWER" in
    "Y"|"y" )
        echo "NAME :            $NAME" >> empl.txt
        echo "AGE :             $AGE" >> empl.txt
        echo "DEPARTMENT :      $DEPARTMENT" >> empl.txt
        echo "==============================================="
        echo "Your data were saved into employee file"
        CHECK=1
        ;;
    N|n )
        echo "Nothing was saved, run the script again if you want to add data to employee file"
        CHECK=1
        ;;
    * )
        echo "Wrong answer provided"
        ;;
esac
done
    

