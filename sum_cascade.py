#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
from unidecode import unidecode
import string
#from Levenshtein import ratio
import nltk
import datetime
import sqlite3 as lite
import os
import re
import sys
from nltk.corpus import stopwords

stopwords = stopwords.words('english')
pattern_split = re.compile(r"\W+")


__author__ = 'Rachel Jin'
__email__ = 'jfang8@cs.vt.edu'


def rewrite():
	with open("./NewYork_reducer.txt", "r") as f, open("./NewYork_cascade.txt", "a") as out:
		for line in f:
			try:
				line = line.strip()
				left = line.split("**")[0]
				count = line.split("**")[1]
				day = left.split(" ")[0]
				hour = left.split(" ")[1]
				compose = "-".join([day, hour])
				
				final = "\t".join([compose, count])
				out.write(final + "\n")

			except:
				continue

rewrite()

def sumcount():
	single = []
	time_list = []
	my_dic = {}
	with open("./NewYork_cascade.txt", "r") as f:
		for line in f:
			line = line.strip()
			left = line.split("\t")[0]
			right = line.split("\t")[1]
			time_list.append(left)
			single.append(int(right))


	for i in range(len(single)-1):
		single[i+1] = single[i+1] + single[i]
	
	for m in range(len(single)):
		print time_list[m], "\t", single[m]
			
sumcount()
