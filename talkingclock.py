# Talking Clock
# (r/dailyprogrammer challenge)
#
# Converts a given time in the format "##:##" from numbers to words.

import inflect
p = inflect.engine()

# Completes and displays the conversion
def time_to_text(time):
	time = time.split(":")

	# Converts given time to integers
	hour = int(time[0])
	minute = int(time[1])

	# Determines a.m. or p.m.
	meridiem = "a.m"
	if hour >= 12:
		meridiem = "p.m"
	
	# Converts Hours
	if hour == 0 or hour == 12:
		hour_text = "twelve "
	elif hour > 12:
		hour = hour % 12
		hour_text = p.number_to_words(hour) + " "
	else:
		hour_text = p.number_to_words(hour) + " "

	# Converts minutes
	if minute == 0:
		minute_text = ""
	elif minute < 10:
		minute_text = "oh " + p.number_to_words(minute) + " "
	else:
		minute_text = p.number_to_words(minute) + " "
	
	# Concatonates full time statement
	time_text = hour_text + minute_text + meridiem

	print(time_text)

	
# Time to be converted is accepted via user input
time = raw_input("Enter time: ")

time_to_text(time)

