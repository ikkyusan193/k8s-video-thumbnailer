#! /bin/bash

input=$1 # sample.mp4
output=$2 # output.gif

filename=$(basename -- "$output")
filename="${filename%.*}" # output


mkdir ./frames/$filename

ffmpeg -ss 30 -t 10 -i $input -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" ./frames/$filename/$filename%01d.bmp
convert -delay 20 -loop 0 ./frames/$filename/$filename*.bmp -layers optimize ./gifs/$output
rm -r ./frames/$filename

## this works
# ffmpeg -ss 30 -t 10 -i $input -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 $output

