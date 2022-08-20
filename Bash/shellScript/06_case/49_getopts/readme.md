6.49 : Manual Parsing vs Getops vs Getop

getops 
    - easy how to parse short positional parameters (-f)
    - does not support long positional parameters (--help)

    - getopts opstring name

OPTIND is initialized to 1 each time the shell or a shell script is invoked.
getopts places index of the next arguemnt to be processed into the variable OPTIND.

getopts
    - parse command options (enhanced)
    - opts = `getopt -o a::b:cde -- long file::, name:, help -- "$@`
    eval set -- "$opts"