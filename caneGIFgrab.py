#!/usr/bin/env python3

''' This script is for downloading the daily precipitable water map gif and puts it into the gif
 "Cane_Archive" folder'''

import os
import datetime
import requests


os.chdir("Cane_Archive")

url = "http://tropic.ssec.wisc.edu/real-time/mtpw2/webAnims/tpw_nrl_colors/natl/mimictpw_natl_latest.gif"

img_name = datetime.datetime.now()
img_name = img_name.strftime("%Y-%m-%d") + ".gif"

with open(img_name, 'wb') as f:
    f.write(requests.get(url).content)





