2.1 ) Intro : What is a script?
    - Nothing more than a sequence of system commands pasted in a file.
        - For Loops
        - Conditional
        - Variables
        - Arguments
        - ... more...?

2.2 ) Invoking the Script
    - ls -l "filename" : shows only details about that specific file.
    - rw-rw-r-- : 
        - first group : owner of the file
        - second group : group file owner
        - third group : other (not first or second)

        - r : read permission (4)
        - w : write permission (2)
        - x : execute permission (1)

        a+* = changing permission for all 3 groups.
        u+* = changing permission for only file owner (second).
        o+* = changing permission for only owner (first).

    - ./"script name" : this runs the script/file 

    - echo $PATH : 

