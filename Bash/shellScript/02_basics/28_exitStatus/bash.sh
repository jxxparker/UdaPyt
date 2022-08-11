#!/bin/bash

VAR=1
let VAR++
let VAR++
echo "var: $VAR"

let VAR++
let VAR++

echo "var: $VAR"
echo "stop"
exit 45

let VAR++
let VAR++
echo "var: $VAR"