from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import json
from pygeocoder import Geocoder
import os
from itertools import *
import math

def encode(s, coding): 
	try:
		return s.decode(coding)
	except:
		return s


def get_DQE_word_cloud(name):
	one = json.load(open("./DQE/"+name+".json", "r"))
	for i in range(300):
		word = one[i][0].encode("utf-8")

		record= ":".join([ word, str(one[i][1]) ])

		with open("./DQE_cloud/"+name, "a") as out:
			out.write(record+"\n")

#get_DQE_word_cloud("20141010")




def get_DQE_top_words():
	whole = []
	for _file in os.listdir("./DQE/"):
		try:
			one = json.load(open("./DQE/"+ _file, "r"))
				
			for i in range(10):				
				whole.append( one[i][0])
		except:
			continue
	print set(whole), len(set(whole))
	for m in set(whole):
		print m
#get_DQE_top_words()



def get_DQE_time_series():
	whole = ['mcguire', 'cancer', 'cdc', 'contagio', 'madrid', 'channel', 'africa', 'usa', 'enfermera', 'aids', 'crisis', 'czar', 'negativo', 'diagnosed', 'est', 'lizzie', 'doctor', 'positive', 'hospital', 'exposed', 'romero', 'mark', 'symptoms', 'health', '#ebola', 'ebola', 'outbreak', 'nurse', 'gets', 'venezuela', 'texas', 'sierra', 'bola', 'case', 'maduro', 'patient', 'ltima', 'cuba', 'masks', 'zuckerberg', 'virus', 'mato', 'millones', 'spreads', 'obama', 'lares', 'liberia', 'brasil', 'joke', 'quarantine', 'dallas', 'frica', 'disease', '@worldstarfunny', 'disney', 'lisis', 'laughs', 'first', 'caso', 'leone', 'travel']

	word_dic = {}
	time_list = ["20140920", "20140921", "20140922","20140923", "20140924", "20140925", "20140926", "20140927", "20140928", "20140929", "20140930", "20141001", "20141002", "20141003", "20141004", "20141005", "20141006", "20141007", "20141008", "20141009", "20141010", "20141011", "20141012", "20141013", "20141013", "20141014", "20141015", "20141016", "20141017", "20141018"]

	# initialize the word dictionary
	for w in whole:
		word_dic[w] = {}
		for t in time_list:
			word_dic[w][t] = 0
	
	for name in time_list:
		one = json.load( open("./DQE/"+name+".json", "r") )
		for h in one:
			if h[0] in word_dic:
				word_dic[ h[0] ][name] = h[1]

	for key in word_dic:
		for day in sorted(word_dic[key]):
			#print key, day, word_dic[key][day]
			record = "\t".join([key, day, str(word_dic[key][day]) ])
			with open("./DQE_word_time_series_excel.txt", "a") as output:
				output.write(record + "\n")
		
	
	with open("./DQE_word_time_series.json", "w") as out:
		json.dump(word_dic, out)		
#get_DQE_time_series()



	




"get each country's time series: #2014-09-28|United States_Washington_King**1"
def get_country_timeseries():
	country_dic = {}
		
	for _file in os.listdir("./rumor_result/weapon/reducer/"):
		try:			
			with open("./rumor_result/weapon/reducer/"+_file, "r") as f:
				for line in f:
					line = line.strip()
					day_loc = line.split("**")[0]
					count = line.split("**")[1]
					day = day_loc.split("|")[0]
					loc_str = day_loc.split("|")[1]			
					country = loc_str.split("_")[0]
					if country not in country_dic:
						country_dic[country] = {}
						country_dic[country][day] = int(count)
					else:
						if day not in country_dic[country]:
							country_dic[country][day] = int(count)					
						else:
							country_dic[country][day] = country_dic[country][day] + int(count)
		except:
			continue
					
	with open("./all_country_weapon_timeseries.json", "w") as out:
		json.dump(country_dic, out)							
#get_country_timeseries()

	
def plot_time_series(country):
	whole = json.load(open("./all_country_weapon_timeseries.json","r"))
	c_list = []
	
	for day in sorted(whole[country]):
		print day, whole[country][day]
		c_list.append(whole[country][day])			
#plot_time_series("France")



def get_all_cascade():
	whole = json.load(open("./all_country_weapon_timeseries.json","r"))
	c_dic = {"2014-09-01":0, "2014-09-02":0, "2014-09-03":0, "2014-09-04":0, "2014-09-05":0, "2014-09-06":0, "2014-09-07":0, "2014-09-08":0, "2014-09-09":0,"2014-09-10":0, "2014-09-11":0, "2014-09-12":0,"2014-09-13":0, "2014-09-14":0, "2014-09-15":0, "2014-09-16":0, "2014-09-17":0,"2014-09-18":0, "2014-09-19":0, "2014-09-20":0, "2014-09-21":0, "2014-09-22":0,"2014-09-23":0, "2014-09-24":0, "2014-09-25":0, "2014-09-26":0, "2014-09-27":0, "2014-09-28":0, "2014-09-29":0, "2014-09-30":0, "2014-10-01":0, "2014-10-02":0, "2014-10-03":0, "2014-10-04":0, "2014-10-05":0, "2014-10-06":0, "2014-10-07":0, "2014-10-08":0, "2014-10-09":0, "2014-10-10":0, "2014-10-11":0, "2014-10-12":0, "2014-10-13":0, "2014-10-13":0, "2014-10-14":0, "2014-10-15":0, "2014-10-16":0, "2014-10-17":0, "2014-10-18":0}
	c_list = ["20140901", "20140902", "20140903", "20140904", "20140905", "20140906", "20140907", "20140908", "20140909","20140910", "20140911", "20140912","20140913", "20140914", "20140915", "20140916", "20140917","20140918", "20140919", "20140920", "20140921", "20140922","20140923", "20140924", "20140925", "20140926", "20140927", "20140928", "20140929", "20140930", "20141001", "20141002", "20141003", "20141004", "20141005", "20141006", "20141007", "20141008", "20141009", "20141010", "20141011", "20141012", "20141013", "20141013", "20141014", "20141015", "20141016", "20141017", "20141018"]
	single = []
	for c in whole:		
		for day in whole[c]:
			c_dic[day] = c_dic[day] + int(whole[c][day])
	for k in sorted(c_dic):
		single.append(c_dic[k])
	
	for i in range(len(single)-1):
		single[i+1] = single[i+1] + single[i]
	
	for m in range(len(single)):
		print c_list[m], "\t", single[m]
#get_all_cascade()
			

	

# used for SEIZ model
def get_rumor_cascade(rumorId):
	num_dic = {}
	for _file in os.listdir("./rumor_result/"+rumorId+"/reducer/"):		
		num = 0
		try:			
			with open("./rumor_result/"+rumorId+"/reducer/"+_file, "r") as f:	
				for line in f:
					try:
						line = line.strip()
						count = int(line.split("**")[1])
						before = line.split("**")[0]
						day = before.split("|")[0]
						num = num + count
					except:
						continue				
				if day not in num_dic:
					num_dic[day] = num				
		except:
			continue	

	c_list = ["20140928", "20140929", "20140930", "20141001", "20141002", "20141003", "20141004", "20141005", "20141006", "20141007", "20141008", "20141009", "20141010", "20141011", "20141012", "20141013", "20141013", "20141014", "20141015", "20141016", "20141017", "20141018"]
	single = []

	for k in sorted(num_dic):
		single.append(num_dic[k])
	
	for i in range(len(single)-1):
		single[i+1] = single[i+1] + single[i]
	
	for m in range(len(single)):
		print c_list[m], "\t", single[m]


#get_rumor_cascade("12")






# 2014-10-08|United States_Nevada_Clark**1
def read_city_state():
	map_dic = json.load(open("./map_dic/map_lat_lon_20141008.json"))
	#2014-10-18|Australia_Australian Capital Territory_Majura**1
	new_dic = {}

	for _file in os.listdir("./rumor_result/20141008/"):
		try:			
			with open("./rumor_result/20141008/"+_file, "r") as f:	
				for line in f:
					try:
						line = line.strip()
						day_loc = line.split("**")[0]						
						loc_str = day_loc.split("|")[1]
						loc_str = loc_str.strip()				
						state = loc_str.split("_")[1]
						country = loc_str.split("_")[0]

						if len(state)>1:						
							if loc_str not in map_dic:
								new_dic[loc_str] = {}	
								results = Geocoder.geocode(loc_str)				
								new_dic[loc_str]["lat"] = results[0].coordinates[0]
								new_dic[loc_str]["lon"] = results[0].coordinates[1]
							else:
								if map_dic[loc_str] == {} :						
									results = Geocoder.geocode(loc_str)				
									new_dic[loc_str]["lat"] = results[0].coordinates[0]
									new_dic[loc_str]["lon"] = results[0].coordinates[1]
								else:
									new_dic[loc_str] = map_dic[loc_str]
				
							
					except:
						continue
		except:
			continue

	with open("./map_dic/map_lat_lon_20141008_state.json", "w") as out:
		json.dump(new_dic, out)


# 2014-10-08|United States_Nevada_Clark**1
def read_city_country():
	map_dic = json.load(open("./map_dic/map_lat_lon_20141008_state.json"))
	#new_dic = {}

	for _file in os.listdir("./rumor_result/20141008/"):
		try:			
			with open("./rumor_result/20141008/"+_file, "r") as f:	
				for line in f:
					try:
						line = line.strip()
						day_loc = line.split("**")[0]						
						loc_str = day_loc.split("|")[1]
						loc_str = loc_str.strip()				
						state = loc_str.split("_")[1]
						country = loc_str.split("_")[0]
					
						if len(state)<=1:							
							map_dic[loc_str] = {}	
							results = Geocoder.geocode(loc_str)				
							map_dic[loc_str]["lat"] = results[0].coordinates[0]
							map_dic[loc_str]["lon"] = results[0].coordinates[1]					
							
					except:
						continue
		except:
			continue

	with open("./map_dic/map_lat_lon_20141008_country.json", "w") as out:
		json.dump(map_dic, out)



#read_city_country()





def second_run_map():
	map_dic = json.load(open("./map_dic/map_lat_lon_20141018_0.json"))
	for key in map_dic:	
		if map_dic[key] == {}:
			results = Geocoder.geocode(key)				
			map_dic[key]["lat"] = results[0].coordinates[0]
			map_dic[key]["lon"] = results[0].coordinates[1]

	with open("./map_dic/map_lat_lon_20141018.json", "w") as out:
		json.dump(map_dic, out)




#2014-10-18|Australia_Australian Capital Territory_Majura**1
def get_lat_lon_count(filepath, map_file):
	lons = []
	lats = []
	magnitudes = []
	map_dic = json.load(open(map_file))

	with open(filepath, "r") as f:
		for line in f:
			try:
				line = line.strip()
				day_loc = line.split("**")[0]
				count = line.split("**")[1]
				loc_str = day_loc.split("|")[1]

				if loc_str in map_dic:				
					lat = map_dic[loc_str]["lat"]
					lon = map_dic[loc_str]["lon"]
				
					lats.append(lat)
					lons.append(lon)
					magnitudes.append(float(count))
			except:
				continue
	return lats, lons, magnitudes 




def plot_rumor_map(day, day1):	
	map = Basemap(projection='robin', lat_0=0, lon_0=-100, resolution='l', area_thresh=1000.0)
	#map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution = 'h')
		 
	map.drawcoastlines()
	map.drawcountries()	
	map.fillcontinents(color='white')
	map.drawmapboundary()
	map.drawstates()
	 
	map.drawmeridians(np.arange(0, 360, 30))
	map.drawparallels(np.arange(-90, 90, 30))

	# x,y = m(lon, lat)
	# points = m.scatter(x,y,zorder=3,s=sizes, c=colors, alpha=0.9)

	lats1, lons1, magnitudes1 = get_lat_lon_count("./rumor_result/1/reducer/1_"+day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")	
	
	min_marker_size = 1
	for lon, lat, mag in zip(lons1, lats1, magnitudes1):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'rD', markersize=msize, alpha=0.9, label='iphone') #, markerfacecolor="None"

		

	lats2, lons2, magnitudes2 = get_lat_lon_count("./rumor_result/2/reducer/2_"+ day+"_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons2, lats2, magnitudes2):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'g*', markersize=msize, alpha=0.9, label='zombies')


	lats3, lons3, magnitudes3 = get_lat_lon_count("./rumor_result/3/reducer/3_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons3, lats3, magnitudes3):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'bo', markersize=msize, alpha=0.9)	


	lats4, lons4, magnitudes4 = get_lat_lon_count("./rumor_result/4/reducer/4_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons4, lats4, magnitudes4):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'c*', markersize=msize, alpha=0.9)


	lats5, lons5, magnitudes5 = get_lat_lon_count("./rumor_result/5/reducer/5_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons5, lats5, magnitudes5):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'y<', markersize=msize)

	lats6, lons6, magnitudes6 = get_lat_lon_count("./rumor_result/6/reducer/6_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons6, lats6, magnitudes6):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'co', markersize=msize, alpha=0.9)


	lats7, lons7, magnitudes7 = get_lat_lon_count("./rumor_result/7/reducer/7_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons7, lats7, magnitudes7):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'mo', markersize=msize, alpha=0.9)


	lats9, lons9, magnitudes9 = get_lat_lon_count("./rumor_result/9/reducer/9_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons9, lats9, magnitudes9):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'rx', markersize=msize, alpha=0.9)


	lats11, lons11, magnitudes11 = get_lat_lon_count("./rumor_result/11/reducer/11_"+day+"_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons11, lats11, magnitudes11):
		x,y = map(lon, lat)
		msize =  10* math.log(mag) * min_marker_size
		map.plot(x, y, 'yo', markersize=msize, alpha=0.9)


	lats12, lons12, magnitudes12 = get_lat_lon_count("./rumor_result/12/reducer/12_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+"_country.json")
	for lon, lat, mag in zip(lons12, lats12, magnitudes12):
		x,y = map(lon, lat)
		msize = 10* math.log(mag) * min_marker_size
		map.plot(x, y, 'ro', markersize=msize, alpha=0.9)	
	

	#title_string = "Top 10 category rumors about Ebola on %s " % (day1)
	title_string = " %s " % (day1)
	plt.title(title_string) 

	
	plt.show()
	#plt.show()
	#from matplotlib.backends.backend_pdf import PdfPages
	#pp = PdfPages(day)
	#plt.savefig(pp, format='pdf')
	#pp.close()

	#plt.savefig(day)
	
#plot_rumor_map("20140929", "2014-09-29")
#plot_rumor_map("20140930", "2014-09-30")
#plot_rumor_map("20141008", "2014-10-08")

"""
plot_rumor_map("20140928", "2014-09-28")
plot_rumor_map("20140930", "2014-09-30")
plot_rumor_map("20141001", "2014-10-01")
plot_rumor_map("20141002", "2014-10-02")
plot_rumor_map("20141003", "2014-10-03")
plot_rumor_map("20141008", "2014-10-08")
plot_rumor_map("20141010", "2014-10-10")
plot_rumor_map("20141012", "2014-10-12")
plot_rumor_map("20141013", "2014-10-13")
plot_rumor_map("20141014", "2014-10-14")
plot_rumor_map("20141015", "2014-10-15")
plot_rumor_map("20141016", "2014-10-16")
"""



"""
        b: blue
        g: green
        r: red
        c: cyan
        m: magenta
        y: yellow
        k: black
        w: white
"""


def plot_map():	
	map = Basemap(projection='robin', lat_0=0, lon_0=-100, resolution='l', area_thresh=1000.0)
	#map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution = 'h')
		 
	map.drawcoastlines()
	map.drawcountries()
	map.fillcontinents(color='aqua', lake_color='blue')
	map.drawmapboundary()
	map.drawstates()
	 
	map.drawmeridians(np.arange(0, 360, 30))
	map.drawparallels(np.arange(-90, 90, 30))

	lons = []
	lats = []
	magnitudes = []

	
	with open("./rumor_result/weapon/reducer/20141018_weapon.txt", "r") as f:
		for line in f:
			try:
				line = line.strip()
				loc_str = line.split("**")[0]
				count = line.split("**")[1]
				country = loc_str.split("_")[0]	
				results = Geocoder.geocode(loc_str)

				
				lat = results[0].coordinates[0]
				lon = results[0].coordinates[1]
				
				lats.append(lat)
				lons.append(lon)
				magnitudes.append(float(count))
			except:
				continue			

	min_marker_size = 1
	for lon, lat, mag in zip(lons, lats, magnitudes):
		x,y = map(lon, lat)
		msize = mag * min_marker_size
		map.plot(x, y, 'ro', markersize=msize)
	plt.show()

