# Talking Clock
# Converts and recites the current time.
#
# Based on r/dailyprogrammer challenge

import inflect
import subprocess
from datetime import datetime

p = inflect.engine()

# Converts time to words
def time_to_text(time):
	time = time.split(":")

	hour = int(time[0])
	minute = int(time[1])

	# Determines a.m. or p.m.
	meridiem = "a.m."
	if hour >= 12:
		meridiem = "p.m."

	# Converts hour to words
	if hour == 0 or hour == 12:
		hour_text = "twelve "
	elif hour > 12:
		hour = hour % 12
		hour_text = p.number_to_words(hour) + " "
	else:
		hour_text = p.number_to_words(hour) + " "

	# Converts minutes to words
	if minute == 0:
		minute_text = ""
	elif minute < 10:
		minute_text = "oh " + p.number_to_words(minute) + " "
	else:
		minute_text = p.number_to_words(minute) + " "

	# Combines and returns full time statement
	time_text = "It is" + hour_text + minute_text + meridiem
	return time_text

# Accesses and formats current time
time = str(datetime.now())
time = time.split(" ")
time = time[1]
time = time.split(":")
time = str(time[0]) + ":" + str(time[1])

# Calls os speech function to recite given time.
# the time is converted from numbers to words using
# the time_to_text() function.
subprocess.call(["say", time_to_text(time)])
