#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
from unidecode import unidecode
import string
#from Levenshtein import ratio
import nltk
import datetime
import os
import re
import sys
pattern_split = re.compile(r"\W+")

__author__ = 'Rachel Jin'
__email__ = 'jfang8@cs.vt.edu'

def encode(s, coding): 
	try:
		return s.decode(coding)
	except:
		return s


def twitTimeToDBTime(time):
	TIME_FORMAT = "%a %b %d %H:%M:%S +0000 %Y"
	createdAt = datetime.datetime.strptime(time,TIME_FORMAT)
	return createdAt.strftime("%Y-%m-%d %H:%M:%S")



def	removePunctuations(text):
	for symbol in string.punctuation:
		text = text.replace(symbol," ")
	return text


news_dic = {   "1":["CDC", "confirms"],
		"2":["Dallas"],
		"3":["weapon", "bio-weapon", "manufactured", "manmade", "patent", "patented", "vaccinate" ],
		"4":["white", "black", "skin"],
		"5":["vote", "election"],
		"6":["terrorists","terrorist"],
		"7":["airborne"],
		"8":["Essien", "Essien-Ebola"],
		"9":["hair", "extensions"],
		"10":["Fox"],
		"11":["inject", "suspected", "lethal"],
		"12":["kansas", "Kansas"]
		}



def checkForRumorWords(rumorId, text):
	flag = False    
	text = removePunctuations(text)
	text = text.lower().split()
	for word in rumor_dic["rumorId"]:
		if word in text:
			flag = True
	return flag



def checkrumortokens(rumorId, tokens):
	flag = False	
	for s in tokens:
		for word in rumor_dic[rumorId]:
			if word in s:
				flag = True
	return flag


def checknewstokens(tokens):
	flag = False	
	for s in tokens:		
		#if 'CDC' in s and ('confirmed' in s or 'confirms' or 'diagnosed' in s):
		if 'dallas' in s or 'Dallas' in s:
			flag = True
	return flag



# rumorId
def mapper():
	#data_list = ["20140928", "20140929", "20140930", "20141001", "20141002", "20141003", "20141004", "20141005", "20141006", "20141007", "20141008", "20141009", "20141010", "20141011", "20141012", "20141013", "20141013", "20141014", "20141015", "20141016", "20141017", "20141018" ]
	data_list = ["20140930", "20141001", "20141002"]
	
	for name in data_list:
		try:
			#for _file in os.listdir("/home/jf/Documents/Ebola/raw/" + name):
			for _file in os.listdir("/raid/tskatom/Ebola/Ebola/" + name):
				#with open("/home/jf/Documents/Ebola/raw/"+ name + "/" +_file) as f:
				with open("/raid/tskatom/Ebola/Ebola/"+ name + "/" +_file) as f:					
					for line in f:
						try:
							tweet  = json.loads(line)
									
							text = ""
							userId = ""
							username = ""
							location = ""
							created_at = 0
							postday = 0
							lang = ""
							
		
							text = tweet["text"]
							tokens = tweet["topsy"]["tokens"]
							admin0 = admin1 = admin2 = ""

							tokens = tweet["topsy"]["tokens"]
							if checknewstokens(tokens):				
								#if "tags" in tweet["topsy"]["location"]:
								#	if "admin0" in tweet["topsy"]["location"]["tags"]:
								#		admin0 = tweet["topsy"]["location"]["tags"]["admin0"]
								#		if "admin1" in tweet["topsy"]["location"]["tags"]:
								#			admin1 = tweet["topsy"]["location"]["tags"]["admin1"]
								#		if "admin2" in tweet["topsy"]["location"]["tags"]:
								#			admin2 = tweet["topsy"]["location"]["tags"]["admin2"]
								#		location = "_".join( [admin0.encode("utf-8"), admin1.encode("utf-8"), admin2.encode("utf-8")] )

								created_at = twitTimeToDBTime(tweet["created_at"])
								postday = created_at.strip().split()[0]
								lang = tweet["lang"]
								#if location:
								#	word = 	"|".join([postday, location])				
								#record = "**".join([word, "1"])
		
								with open("./mapper/news/Dallas_mapper_20140930_20141002.txt", "a") as out:
									out.write(record + "\n")
											      
						except:
							print sys.exc_info()
							continue
		except:
			continue


mapper()


