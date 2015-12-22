#!/usr/bin/env python

import datetime
from praytimes import PrayTimes


#Get Prayer Times
#If located in southern hemisphere, use a negative latitude value
#--------------------

#User location
lat = 51.5171
long = 0.1062

#System time and date
now = datetime.datetime.now()

#Prayer time calculation
#Additional options available in praytimes.py
PT = PrayTimes('ISNA') 
times = PT.getTimes((now.year,now.month,now.day), (lat, long), 0,1) 

print times['fajr']
print times['dhuhr']
print times['asr']
print times['maghrib']
print times['isha']

#Update Crontab with Prayer Times
#---------------------------------

from crontab import CronTab

#Function to add azaan time to cron
def addAzaanTime (strPrayerName, strPrayerTime, objCronTab, strCommand):

	job = objCronTab.new(command=strCommand,comment=strPrayerName)
	
	timeArr = strPrayerTime.split(':')

	hour = timeArr[0]
	min = timeArr[1]

	job.minute.on(int(min))
	job.hour.on(int(hour))

	print job

	return

system_cron = CronTab()

strPlayAzaanMP3Command = 'omxplayer -o local /home/pi/Documents/Projects/RPi-Prayer-Alarm/resources/Abdul-Basit.mp3 > /dev/null 2>&1'

jobs = system_cron.find_command(strPlayAzaanMP3Command)

print jobs

for j in jobs:
	system_cron.remove(j) 

addAzaanTime('fajr',times['fajr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('dhuhr',times['dhuhr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('asr',times['asr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('maghrib',times['maghrib'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('isha',times['isha'],system_cron,strPlayAzaanMP3Command)

system_cron.write()





