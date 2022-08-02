2.28 : Exit Status

- We can get return value of a command in following way:
    - command
    - echo $

        - $? will give a return value of previous command
        - the return value is called exit status
        - If the command exits successfully, exit status will be 0, otherwise some non-zero value
        - We can exit a script using exit command
        