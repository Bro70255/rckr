from geopy.distance import geodesic
import json
from math import pi, sin, cos, sqrt, asin,atan2

def find_dist(latlng_1, latlng_2):
	'''
	This function calculate distance in km between two point on Earth
	whose coordinates are passed as two lists and returns rounded distance
	'''
	R=6371
	c1= (latlng_1[0], latlng_1[1])
	c2= (latlng_2[0], latlng_2[1])
	distance = geodesic(c1, c2).km
	return distance

file = "data.json"

with open(file, 'r') as f:
	contries = json.load(f)
first1_20 = { }
for contry in contries:

			if contry['population'] >=6700:
				contries.remove(contry)
				nation_capital = contry['capital']
				population = contry['population']
				co_ordination = contry['latlng']
				moneytype = contry['currencies']

				for moneyname in moneytype:
					mmoney = moneyname['name']
					if moneyname['name'] != "Euro" and moneyname['name'] != "Indian rupee" and moneyname['name'] != "United State Dollar" \
							and moneyname['name'] != "British pound" and moneyname['name'] != "United States dollar" \
							and moneyname['name'] != "Australian dollar" and moneyname['name'] != "West African CFA franc" \
							and moneyname['name'] != "Moroccan dirham" and moneyname['name'] != "East Caribbean dollar" \
							and moneyname['name'] != "Danish krone" and moneyname['name'] != "Central African CFA franc" \
							and moneyname['name'] != "Old Belarusian ruble" and moneyname['name'] != "Japanese yen" \
							and moneyname['name'] != "Chinese yuan" and moneyname['name'] != "Botswana pula" \
							and moneyname['name'] != "Cuban convertible peso" and moneyname['name'] != "Brunei dollar" \
							and moneyname['name'] != "Namibian dollar":
							first1_20[contry['alpha3Code']] = contry['latlng']
							if len(first1_20) == 20:
								result = []
								for i in first1_20:
									if i not in result:
										result.append(i)
								print(result,end="")
								print("\n",first1_20)
								total_dist = 0
								keys = list(first1_20.keys())
								for i in range(len(keys) - 1):
									for j in range(len(keys[i + 1:])):
										total_dist += find_dist(first1_20[keys[i]], first1_20[keys[j]])
										total_dist = round(total_dist, 2)

								print("\n",total_dist)

								break