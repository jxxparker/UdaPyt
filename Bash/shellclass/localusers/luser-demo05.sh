#!/bin/bash

# This script generates a list of random passwords.

# A random number as a password.
PASSWORD="${RANDOM}"
echo "Short Password : ${PASSWORD}"

# Three random numbers together.
PASSWORD="${RANDOM}${RANDOM}${RANDOM}"
echo "Long Password : ${PASSWORD}"

# Use the current date/time as the basis for the password.
PASSWORD="$(date +%s)"
echo "date +%s password : ${PASSWORD}"

# Use nanoseconds to act as randomization.
PASSWORD="$(date +%s%N)"
echo "date +%s%N password : ${PASSWORD}"


# A better password.
PASSWORD=$(date +%s%N | sha256sum | head -c32)
echo "A better password : ${PASSWORD}"

# An even beter password.
PASSWORD=$(date + %s%N${RANDOM}${RANDOM} | sha256sum | head -c48)
echo "An even better password : ${PASSWORD}"

# Append a special character to the password.
SPECIAL_CHARACTER=$(echo '!@#$%^&*()_+=' | fold -w1 | shuf | head -c1)
echo "${PASSWORD}${SPECIAL_CHARACTER}"