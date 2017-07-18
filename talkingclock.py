
# Special Cases:
# 00:00 -> twelve am
# 9:00 -> nine am

import inflect
p = inflect.engine()

def time_to_text(time):
	time = time.split(":")

	hour = int(time[0])
	minute = int(time[1])

	meridiem = "a.m"

	if hour >= 12:
		meridiem = "p.m"

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

	time_text = hour_text + minute_text + meridiem

	print(time_text)

time = raw_input("Enter time: ")
time_to_text(time)

