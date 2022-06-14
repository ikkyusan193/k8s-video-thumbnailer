#! /bin/bash

id=$1 # use id as folder
input=$2 # sample.mp4


filename=$(basename -- "$input")
filename="${filename%.*}" # sample

cd ./scripts
mkdir ./$id

ffmpeg -ss 30 -t 10 -i $input -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" ./$id/$filename%01d.bmp

rm $input


