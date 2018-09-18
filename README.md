# Hurricane scripts

This repository contains scripts relevant to hurricanes

I am particularly interested in compositing hurricane gifs into videos to watch the hurricne season and the developments of the storms as they change week to week. 

I depend on these scripts to download, organize, and transform sattelite data from NOAA into longform videos

## Florence Strikes the Carolinas - Sep 18
[![Florence_video](https://img.youtube.com/vi/QtRf1vUTr38/0.jpg)](http://www.youtube.com/watch?v=QtRf1vUTr38

## How to run these in the Raspberry Pi Crontab

I use my PI Zero server in order to run these jobs daily in the cron.

Type:```bash crontab -e ```

Then append the following line to the file **format accordingly**

```bash
00 00 */1 * * cd /location/dir/of/script/ && python3 python_script.py
```


