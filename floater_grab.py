#!/usr/bin/env python3

''' This script is for downloading the daily gif and putting it into the gif
folder (Floater_arch). Use with crontab

00 00 */1 * * cd /location/of/folder && python3 cron_script.py  <-this code runs the script every night at midnight

'''

import os
import datetime
import requests


os.chdir("Floater_arch")

url ="http://tropic.ssec.wisc.edu/real-time/mimtc/2018_06L/web/gifsBy12hr_12.gif"

img_name = datetime.datetime.now()
img_name = img_name.strftime("%Y-%m-%d") + ".gif"

with open(img_name, 'wb') as f:
    f.write(requests.get(url).content)





