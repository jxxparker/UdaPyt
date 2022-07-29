1.2 ) pwd 

    - pwd : shows current location.

1.3 ) cd

    - cd : transfer you to another directory
    - cd .. : goes one level above your current directory
    - cd - : brings you back to previous directory

1.4 ) ls

    - ls : shows all files insidse directory.
    - ls -l : shows more info about each file.
    - ls -a : show all hidden files.
    - ls -la : show all hidden files and details. ("-l" and "-a" combined)
    - man "any command" : shows how to use all command. (q to exit)

1.5 ) mkdir

    - mkdir : creates a new directory
    - mkdir p : creates directory within directory

1.6 ) touch 

    - touch : creates new file 
    - touch "one file" "two file" : creates multiple files

1.7 ) date

    - date : shows date

1.8 ) cat
    
    - cat : reads the file 
    - cat -n "file name" : reads the file with number of lines
 
1.9 ) rm + rmdir

    - rm "file name" : removes/deletes file
    - rmdir : only deletes empty folders
    - rm -r : removes directories and their contents recursively.

1.10 ) cp 

    - cp "directory/file name" : copies file and pastes it.

1.11 ) mv
    
    - mv : moves file from one directory to another

1.12 ) wc

    - wc : utility displayed the number of lines, word, and bytes contained in each input file, or standard input to the standard output.
    - wc -l "file name" : outputs word count and file name.

1.13 ) grep

    - grep : searches any given input files, selecting lines that match one or more patterns.
    - grep -o "" : only matching( printing only matching part of the lines)
    - grep -v "specific" "file name" : display version information and exit.

1.14 ) find

    - find : find name of the file
    - find /Users/jihunpark/UdaPyt/ -name "*.sh" : searches all files that are ".sh"