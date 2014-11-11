#!/usr/bin/env python

from operator import itemgetter
import sys

#2014-09-30 23**1


current_word = None
current_count = 0
word = None
# 2014-10-04|United States_Oregon_Lane**1

for line in sys.stdin:
	line = line.strip()
	try:
		count = line.split('**')[1]
		word = line.split('**')[0]
		#day = left[0:12]				
	except:
		continue
	try:
		count = int(count)
	except ValueError:
		continue   

	if current_word == word:
		current_count += count
	else:
		if current_word:       
			print '%s**%s' % (current_word, current_count)
       
		current_count = count
		current_word = word

if current_word == word:
	print '%s**%s' % (current_word, current_count)


