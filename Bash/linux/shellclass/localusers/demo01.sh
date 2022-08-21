#!/bin/bash

# This script displays various information to the screen.

# Display 'Hello'
echo 'Hello'

# Assign a value to a variable.
WORD='script'

echo "$WORD"
echo '$WORD'

# combine the variable with hard-coded test.
echo "This is a shell $WORD"

# Display the contents of the variable using an alternative syntax.
echo "This is a shell ${WORD}"

# Append text to the variable.
echo "${WORD}ing is fun!"

# Show how not to append text to a variable.
# This doesn't work:
echo "$WORDing is fun!"

# Create a new variable
ENDING='ed'

# Combine the two variables.
echo "This is ${WORD}-${ENDING}"




