#!/bin/bash

read -p "Your name: " NAME 
read -sp "Your age: " AGE

echo
echo "Name: $NAME, Age: $AGE"

read hOSTNAME < /etc/hostname
echo Hostname: $HOSTNAME