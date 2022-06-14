#! /bin/bash

id=$1 # use id as folder
input=$2 # sample.mp4

filename=$(basename -- "$input")
filename="${filename%.*}" # sample

cd ./scripts

convert -delay 20 -loop 0 ./$id/$filename*.bmp -layers optimize ./gifs/$id.gif
rm -rf ./$id