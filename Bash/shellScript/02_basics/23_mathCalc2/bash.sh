#!/bin/bash
NUMBER=5

#do the NUMBER + 5
# --- let ---
let RESULT=NUMBER+5
echo Result from let: $RESULT

# --- (( )) ---
RESULT=$(( NUMBER + 15 ))
echo "Result from (( )): $RESULT"

# --- [] ---
RESULT=$[ NUMBER + 25 ]
echo Result from [ ]: $RESULT

# --- expr ---
RESULT=$(expr $NUMBER + 35)
echo Result from expr: $RESULT

# # --- bc --- number * 1.9
RESULT=`echo "$NUMBER * 1.9" | bc`
echo Result from bc: $RESULT