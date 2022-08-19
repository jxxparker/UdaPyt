6.46 : Explain Case

case "$VAR" in

"$condition1" )
    command(s)...
    ;;

"$condition2" )
    command(s)...
    ;;

*)

command(s)...
;;

esac



case "$(whoami)" in
"root")
    echo you are root
    ;;
    