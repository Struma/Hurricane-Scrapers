# Hurricane scripts

This repository contains scripts relevant to hurricanes

I am particularly interested in compositing hurricane gifs into videos to watch the hurricne season and the developments of the storms as they change week to week. 

I depend on these scripts to download, organize, and transform sattelite data from NOAA into longform videos

## Florence Strikes the Carolinas - Sep 2018
[![Florence_video](https://img.youtube.com/vi/QtRf1vUTr38/0.jpg)](http://www.youtube.com/watch?v=QtRf1vUTr38)

## How to run these in the Raspberry Pi Crontab

I use my PI Zero server in order to run these jobs daily in the cron.

Type:

```crontab -e ```

Then append the following line to the file. **Don't forget to format accordingly**

```bash
00 00 */1 * * cd /location/dir/of/scripts_dir/ && python3 python_script.py
```
The cd command precedes the python script because the crontab doesn't operate exactly the same as in a virtual terminal. If you **don't need to call file operations** like saving or creating directories, you'll be fine. Otherwise, using explicit links in your code should also work. 

Most of my code is written with symbolic links referenced to a arbirtary top level directory. I use the cd program to navigate to the top level directory in the cron, and then I call the python script which then executes from the proper location.

