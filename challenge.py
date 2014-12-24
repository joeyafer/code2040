#Returns a reversed string
def reverseString(n):
	return n[::-1]

#Returns the index to a key 'needle' with the array 'haystack'
def findInHaystack(needle, haystack):
	return haystack.index(needle)

#Returns an array filtered by those that do not begin with the string 'prefix'
def prefixFilter(prefix, words):
	result = []
	for word in words:
		if word.startswith(prefix) == False:
			result.append(word)
	return result

#Returns a string datestamp, formatted to ISO 8601, incresed by the int 'interval' in seconds
def addSeconds(datestamp, interval):
	year = ''
	month = ''
	day = ''
	hour = ''
	minute = ''
	seconds = ''
	count = 0;
	for n in datestamp:
		if count < 4:
			year = year + n
		elif count >= 5 and count < 7:
			month = month + n
		elif count >= 8 and count < 10:
			day = day + n
		elif count >= 11 and count < 13:
			hour = hour + n
		elif count >= 14 and count < 16:
			minute = minute + n
		elif count >=17 and count < 19:
			seconds = seconds + n
		count += 1
	date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(seconds))
	date = date + datetime.timedelta(seconds=interval)
	return date.isoformat() + '.000Z'

import requests
import datetime
from datetime import timedelta
#Setup
values = {'email' : 'joeyaf7@stanford.edu',
          'github' : 'https://github.com/joeyafer/code2040.git' }
req = requests.post('http://challenge.code2040.org/api/register', json=values)
next = req.json()
code2040_id = next['result']
values = {'token': code2040_id}

#First Stage
stage_one = requests.post('http://challenge.code2040.org/api/getstring', json=values)
first = stage_one.json()
string = reverseString(first['result'])
values['string'] = string
stage_one = requests.post('http://challenge.code2040.org/api/validatestring', json=values)
del values['string']

#Second Stage
stage_two = requests.post('http://challenge.code2040.org/api/haystack', json=values)
second = stage_two.json()
index = findInHaystack(second['result']['needle'], second['result']['haystack'])
values['needle'] = index
stage_two = requests.post('http://challenge.code2040.org/api/validateneedle', json=values)
del values['needle']

#Third Stage
stage_three = requests.post('http://challenge.code2040.org/api/prefix', json=values)
third = stage_three.json()
array = prefixFilter(third['result']['prefix'], third['result']['array'])
values['array'] = array
stage_three = requests.post('http://challenge.code2040.org/api/validateprefix', json=values)
del values['array']

#Fourth Stage
stage_four=requests.post('http://challenge.code2040.org/api/time', json=values)
fourth = stage_four.json()
datestamp = addSeconds(fourth['result']['datestamp'], fourth['result']['interval'])
values['datestamp'] = datestamp
stage_four = requests.post('http://challenge.code2040.org/api/validatetime', json=values)
del values['datestamp']

#Checking my grades
check_grades = requests.post('http://challenge.code2040.org/api/status', json=values)
grades = check_grades.json()
print grades












