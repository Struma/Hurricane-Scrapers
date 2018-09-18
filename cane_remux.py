#!/usr/bin/env python3

#this is a short script that will do the simple task of reading in gif images and
#creating long video animations from them. Also manages archives of scraped gifs

import os               #to move around
import glob             #to grab up image in a dir
from PIL import Image, GifImagePlugin
import subprocess


counter = 0

working_folder = ['temp/', 'Prec_water_videos/', 'Prec_water_arch/',
"Prec_water_scrapes/"]

ffmpeg = "ffmpeg -f image2 -r 15 -i '%d.png' ../Prec_water_videos/"

seq = range(5,29) #The range of GIF frames that are animated


#create all the folder if they don't exist
for folder in working_folder:
    if not os.path.exists(folder):
        os.makedirs(folder)

os.chdir(working_folder[3])     #switch into the animations folder
file_list = glob.glob('*.gif')  #grab all pngs
list.sort(file_list)

for pic in file_list:
    img_obj = Image.open(pic) 
    for frame in seq:            #range(0,img_obj.n_frames):
        img_obj.seek(frame)
        filename = str(counter) + ".png"
        img_obj.save("../temp/"+filename, "PNG")
        counter = counter + 1

begin = file_list[0]
end = file_list[len(file_list)-1]
video_name = begin.split(".")[0] + "_" + end.split("-")[1] + "-" + end.split("-")[2].split(".")[0]


mpeg_call = ffmpeg +  video_name + ".mp4"

os.chdir("../temp/") #switch to the folder with all the images
subprocess.call(mpeg_call, shell=True)

os.chdir("../")
subprocess.call('rm -rf temp', shell=True)
os.chdir(working_folder[3])

for item in file_list:
    os.rename(item, "../" + working_folder[2] + item)
