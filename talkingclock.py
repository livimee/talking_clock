# Talking Clock

import inflect
import subprocess
from datetime import datetime

p = inflect.engine()

def time_to_text(time):
	time = time.split(":")

	hour = int(time[0])
	minute = int(time[1])

	meridiem = "a.m."

	if hour >= 12:
		meridiem = "p.m."

	if hour == 0 or hour == 12:
		hour_text = "twelve "
	elif hour > 12:
		hour = hour % 12
		hour_text = p.number_to_words(hour) + " "
	else:
		hour_text = p.number_to_words(hour) + " "

	if minute == 0:
		minute_text = ""
	elif minute < 10:
		minute_text = "oh " + p.number_to_words(minute) + " "
	else:
		minute_text = p.number_to_words(minute) + " "

	time_text = "It is" + hour_text + minute_text + meridiem

	return time_text

time = str(datetime.now())
time = time.split(" ")
time = time[1]
time = time.split(":")
time = str(time[0]) + ":" + str(time[1])

subprocess.call(["say", time_to_text(time)])
