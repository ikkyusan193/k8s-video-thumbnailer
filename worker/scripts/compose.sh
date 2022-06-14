#! /bin/bash

input=$1 # sample.mp4
output=$2 # output.gif

filename=$(basename -- "$input")
filename="${filename%.*}" # sample

cd ./scripts

convert -delay 20 -loop 0 ./$filename/$filename*.bmp -layers optimize ./gifs/$output
rm -rf ./$filename