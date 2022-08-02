2.26 : Redirection and piping

- Every program we run on the command line automatically has three data streams
    - STDIN (0) - Standard input (data provided to program)
    - STDOUT(1) - Standard output (what program prints, defaulty to the terminal)
    - STDERR(2) - Standard error (what error messages program prints, defaulty to the terminal)

- Examples : cat file1.txt>output_from_cat.txt
             cat file1.txt 1>output_from_cat.txt
             cat file1.txt 2>errors.txt
             cat file1.txt 1>output_from_cat.txt 2>errors.txt
             cat file1.txt &> output_from_cat.txt
             cat file1.txt 1> output_from_cat.txt2>&1

            