#RPi-Prayer-Alarm
-
##Overview
This repository contains python scripts to automate a dynamic alarm system for the [Muslim prayer calls which occurs 5 times a day](https://en.wikipedia.org/wiki/Salah) on a Raspberry Pi.

###Disclaimer
This tool was originally sourced from a shared dropbox folder and has been uploaded to github for easier tracking. [Post by original Author](http://randomconsultant.blogspot.co.uk/2013/07/turn-your-raspberry-pi-into-azaanprayer.html).

#####Original Copyright Block
```
praytimes.py: Prayer Times Calculator (ver 2.3)
Copyright (C) 2007-2011 PrayTimes.org

Python Code: Saleem Shafi, Hamid Zarrabi-Zadeh
Original js Code: Hamid Zarrabi-Zadeh

License: GNU LGPL v3.0

TERMS OF USE:
	Permission is granted to use this code, with or
	without modification, in any website or application
	provided that credit is given to the original work
	with a link back to PrayTimes.org.

This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY.
```

##Prerequisites
1. Raspberry Pi Raspbian OS (other OS's haven't been tested)
2. Cron
2. Python crontab library

#Setup
##1.0 Define user location and preferences
In the getAzaanTimers.py file:

1. User geographical location: longitude `long` and latitude `lat`. *Note: if you're in the southern hemisphere, use a negative latitude value.*
2. Prayer calculation method: `PT = PrayTimes('METHOD') `
3. User time-zone, example 10+DMT with daylight savings: `times = PT.getTimes((now.year,now.month,now.day), (lat, long), 10,1) `

##2.0 Schedule cron job
Add following job to your cron:

```
# m h	dom mon dow command
0 1 * * * python /home/pi/Documents/Projects/RPi-Prayer-Alarm/resources/Abdul-Basit.mp3 > /dev/null 2>&1
```

##3.0 Check everything works

### Check prayer-time calculation is correct

`python /home/pi/Documents/Projects/RPi-Prayer-Alarm/getAzaanTimers.py`

### Check Raspberry Pi is outputing audio
`omxplayer /home/pi/Documents/Projects/RPi-Prayer-Alarm/resources/Abdul-Basit.mp3`

#### Adjust Raspberry Pi output volume from headphone jack

Add the following to your .bashrc file:

```
# Increase volume by 5%
alias volu='sudo amixer set PCM -- $[$(amixer get PCM|grep -o [0-9]*%|sed 's/%//')+5]%'
# Decrease volume by 5%
alias vold='sudo amixer set PCM -- $[$(amixer get PCM|grep -o [0-9]*%|sed 's/%//')-5]%'
```

Reload bashrc: `. ~/.bashrc`