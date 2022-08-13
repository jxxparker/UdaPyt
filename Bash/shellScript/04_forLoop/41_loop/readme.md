41 : Loops

- A loop is a block of code that iterates a list of commands as 
long as the loop control condition is true

example :
for arg in [list]                   - for PLANET in Mercury Venus Earth
do                                  - do
    commands(s) ...                 -   echo $PLANET
done                                - done

                                    $ Mercury 
                                    # Venus
                                    # Earth
                                    IFS=$'\t\n'

for FILE in *.txt
do
    echo $FILE
done