#!/bin/bash

read -p "Your name: " NAME 
read -sp "Your age: " AGE # cannot see whats happening

echo
echo "Name: $NAME, Age: $AGE"

read HOSTNAME < /etc/hostname
echo Hostname: $HOSTNAME