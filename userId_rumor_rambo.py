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


rumor_dic = {   "1":["iphone"],
		"2":["rose", "zombie", "zombies"],
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


rumor_list = ["iphone",	"rose", "zombie", "zombies", "weapon", "bio-weapon", "manufactured", "manmade", "patent", "patented", "white", "black", "skin", "vote", "election", "terrorists","terrorist",
		"airborne", "Essien", "Essien-Ebola", "hair", "extensions", "Fox", "inject", "suspected", "lethal"]
 

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



# make user of URL?
# pick 3 days, show their evolution
def network_ids(name, rumorId):
	for _file in os.listdir("/raid/tskatom/Ebola/Ebola/"+name):
	#for _file in os.listdir("./raw/"+name):
		try:			
			with open("/raid/tskatom/Ebola/Ebola/"+ name + "/" +_file, "r") as f:
			#with open("./raw/"+ name + "/" +_file, "r") as f:					
				for line in f:
					try:
						tweet  = json.loads(line)						
						tokens = ""
						userId = username = lang = location = admin0 = admin1 = admin2 = ""
						created_at = postday = 0
						re_created_at = 0							
						re_location = "" # the original source id
						reply_usid = ""	
						retweet_userid = ""			
		
						tokens = tweet["topsy"]["tokens"]
						if checkrumortokens(rumorId, tokens):						

							if "id_str" in tweet["user"]:
								userId = tweet["user"]["id_str"] #624553775
								#username = tweet["user"]["screen_name"]	
								
							if "created_at" in tweet:
								created_at = twitTimeToDBTime(tweet["created_at"])
								postday = created_at.strip().spli[0]
											
							if tweet["in_reply_to_user_id"]:
								reply_usid = tweet["in_reply_to_user_id"]				
				
							if "retweeted_status" in tweet:
								re_created_at = tweet["retweeted_status"]["created_at"]
								re_created_at = twitTimeToDBTime(re_created_at)
								if "user" in tweet["retweeted_status"]:
									retweet_userid = tweet["retweeted_status"]["user"]["id_str"]

							strings = [userId, reply_usid, retweet_userid]
							
							if reply_usid or retweet_userid:	
								record = "\t".join(x for x in strings if x)
								
								with open("./rumor_id/"+ rumorId+ "_"+ "rumor_userid_" + name, "a") as out:
									out.write(record+"\n")					
									      
					except:
						print sys.exc_info()
						continue
		except:
			continue


network_ids("20141006","1")
network_ids("20141013","1")
network_ids("20141020","1")
network_ids("20141027","1")

network_ids("20141006","2")
network_ids("20141013","2")
network_ids("20141020","2")
network_ids("20141027","2")


network_ids("20141006","3")
network_ids("20141013","3")
network_ids("20141020","3")
network_ids("20141027","3")


network_ids("20140930","4")
network_ids("20141013","4")
network_ids("20141020","4")
network_ids("20141027","4")


"""
network_ids("20140930","5")
network_ids("20141006","5")
network_ids("20141020","5")
network_ids("20141027","5")


network_ids("20141006","6")
network_ids("20141013","6")
network_ids("20141020","6")
network_ids("20141027","6")



network_ids("20140930","7")
network_ids("20141006","7")
network_ids("20141020","7")
network_ids("20141027","7")


network_ids("20140930","9")
network_ids("20141006","9")
network_ids("20141020","9")
network_ids("20141027","9")


network_ids("20140930","11")
network_ids("20141006","11")
network_ids("20141013","11")
network_ids("20141020","11")
network_ids("20141027","11")


network_ids("20140930","12")
network_ids("20141006","12")
network_ids("20141020","12")
network_ids("20141027","12")
"""
