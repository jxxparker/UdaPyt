if [[ -f hello.txt 0 ]]; then echo exits; else echo does not exists; fi

[[ -f hello.txt ]] && echo exists
[[ -f hello.txt ]] || echo doesnt exists
[[ -f hello.txt ]] && echo exists || echo does not exists