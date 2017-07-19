# Talking Clock
r/dailyprogammer challenge [EASY]

https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

Problem Info:
---------------------------------------------------

**Description:**

No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.


**Input Description:**

An hour (0-23) followed by a colon followed by the minute (0-59).


**Output Description:**

The time in words, using 12-hour format followed by am or pm.


**Sample Input data:**

00:00

01:30

12:05

14:01

20:29

21:00


**Sample Output data:**

It's twelve am

It's one thirty am

It's twelve oh five pm

It's two oh one pm

It's eight twenty nine pm

It's nine pm


**Extension challenges (optional):**

Add voice: http://steve-audio.net/voices/



Solution Info:
---------------------------------------------------
**Modules used:**

inflect.py: https://pypi.python.org/pypi/inflect
(to convert numbers to words)

subprocess
(to access os speech function)

datetime
(to access current time)


**? ? ?**

Doesn't work unless these commands are executed in terminal first:


export PATH="/usr/local/opt/python/libexec/bin:$PATH"

pip install -e git+https://github.com/pwdyson/inflect.py#egg=inflect

**? ? ?**

The number to word part isn't necessary for the speech part.

I could simplify it by just keeping the numbers in string format (i.e. "12")

PROBABLY ONLY WORKS ON MAC ATM
