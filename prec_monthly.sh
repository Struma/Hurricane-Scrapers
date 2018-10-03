#!/bin/bash

#> vid_list.txt;

ls 20*.mp4 | sort  > vid_list.log;

diff old_list.log vid_list.log | grep '> ' | sed 's/> //' | sort | gawk '{ print "file","\047"$1"\047"}' > dif_list.log;

cat vid_list.log  > old_list.log;

filename=$(date +"%m");
flnmYear=$(date +"%y");
declare -A months;
months=( [1]="Jan" [2]="Feb" [3]="Mar" [4]="Apr" [5]="May" [6]="Jun" [7]="Jul" [8]="Aug" [9]="Sep"
        [10]="Oct" [11]="Nov" [12]="Dec")

filename=$[$filename-1];

final_name=${months[$filename]}$flnmYear.mp4;

ffmpeg -f concat -i dif_list.log -c copy $final_name;

rm vid_list.log;
