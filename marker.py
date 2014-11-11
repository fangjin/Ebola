import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



x1 = 10
y1 = 100
x2 = 2
y2 = 2
x3=20
y3=20
x4=25
y4=25

plt.plot(x1, y1, "rD", label="iphone", markersize=12)
plt.plot(x2, y2, "g*", label="zombies", markersize=17)
plt.plot(x3, y3, "bo", label="patent", markersize=15)
plt.plot(x4, y4, "c*", label="white", markersize=17)
plt.plot(x1, y1, "y<", label="vote", markersize=15)
plt.plot(x2, y2, "co", label="terrorist", markersize=15)
plt.plot(x3, y3, "mo", label="airborne", markersize=15)

plt.plot(x3, y3, "rx", label="hair", markersize=15)

plt.plot(x4, y4, "yo", label="inject", markersize=15)
plt.plot(x4, y4, "ro", label="kansas", markersize=15)

lg=plt.legend()
lg.draw_frame(False)

plt.show()

"""


	lats6, lons6, magnitudes6 = get_lat_lon_count("./rumor_result/6/reducer/6_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+".json")
	for lon, lat, mag in zip(lons6, lats6, magnitudes6):
		x,y = map(lon, lat)
		msize = 5* math.log(mag) * min_marker_size
		map.plot(x, y, 'co', markersize=msize, alpha=0.9)


	lats7, lons7, magnitudes7 = get_lat_lon_count("./rumor_result/7/reducer/7_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+".json")
	for lon, lat, mag in zip(lons7, lats7, magnitudes7):
		x,y = map(lon, lat)
		msize = 5* math.log(mag) * min_marker_size
		map.plot(x, y, 'mo', markersize=msize, alpha=0.9)


	lats9, lons9, magnitudes9 = get_lat_lon_count("./rumor_result/9/reducer/9_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+".json")
	for lon, lat, mag in zip(lons9, lats9, magnitudes9):
		x,y = map(lon, lat)
		msize = 5* math.log(mag) * min_marker_size
		map.plot(x, y, 'rx', markersize=msize, alpha=0.9)


	lats11, lons11, magnitudes11 = get_lat_lon_count("./rumor_result/11/reducer/11_"+day+"_reducer.txt", "./map_dic/map_lat_lon_"+ day+".json")
	for lon, lat, mag in zip(lons11, lats11, magnitudes11):
		x,y = map(lon, lat)
		msize =  5* math.log(mag) * min_marker_size
		map.plot(x, y, 'yo', markersize=msize, alpha=0.9)


	lats12, lons12, magnitudes12 = get_lat_lon_count("./rumor_result/12/reducer/12_"+ day+ "_reducer.txt", "./map_dic/map_lat_lon_"+ day+".json")
	for lon, lat, mag in zip(lons12, lats12, magnitudes12):
		x,y = map(lon, lat)
		msize = 5* math.log(mag) * min_marker_size
		map.plot(x, y, 'ro', markersize=msize, alpha=0.9)	
	

	title_string = "Top 10 category rumors about Ebola on %s " % (day1)
	plt.title(title_string) 
"""

