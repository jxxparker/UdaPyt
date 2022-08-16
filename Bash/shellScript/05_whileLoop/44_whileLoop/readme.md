5.44 : While Loop

while [ condition ] 
do
    command(s) ...
done


while [ "$NAME" != "stop" ] 
do
    echo -n Enter your name:
    read NAME
done
