#!/bin/bash

ls *.mp4 | sort | tail > vid_list.txt;

diff old_list.txt vid_list.txt | grep '> ' | sed 's/> //' | sort > dif_list.txt;

cat vid_list.txt  > old_list.txt;

filename=$(date +"%m");
flnmYear=$(date +"%y");
declare -A months;
months=( [1]="Jan" [2]="Feb" [3]="Mar" [4]="Apr" [5]="May" [6]="Jun" [7]="Jul" [8]="Aug" [9]="Sep"
        [10]="Oct" [11]="Nov" [12]="Dec")

filename=$[$filename-1];

final_name=${months[$filename]}$flnmYear.mp4;

ffmpeg -f concat -i dif_list.txt -c copy $final_name;

rm vidlist.txt
