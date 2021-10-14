from pandas import read_csv
from sys import argv

import matplotlib.pyplot as plt

def		estimate_price(km, t0, t1):
	return (km * t1 + t0)

def		train(km, price):
	N = float(len(km))
	learning_rate = 0.1
	t0 = 0.0
	t1 = 0.0

	for i in range(0, 1000):
		pred = estimate_price(km, t0, t1)
		tmp0 = .0
		tmp1 = .0
		for j in range(int(N)):
			tmp0 += pred[j] - price[j]
			tmp1 += (pred[j] - price[j]) * km[j]
		t0 -= learning_rate * ((1.0 / N) * tmp0)
		t1 -= learning_rate * ((1.0 / N) * tmp1)
	return (t0, t1)

def		save(t0, t1, min_km, max_km, min_price, diff_price):
	p1 = t0 * diff_price + min_price
	p2 = (t1 + t0) * diff_price + min_price
	t1 = (p2 - p1) / (max_km - min_km)
	t0 = -(max_km * t1 - p2)

	with open("./values", 'w') as file:
		file.write("{0}\n{1}".format(t1, t0))
			
if __name__ == "__main__":
	try:
		data = read_csv("./data.csv")
	except:
		print("data.csv not found")
		exit(-1)
	try:
		km = data["km"]
		price = data["price"]
		if (len(km) != len(price) or len(price) <= 1 or len(km) <= 1):
			raise Exception
	except:
		print("not enough data")
		exit(-1)

	if ("-plot" in argv):
		plt.scatter(km, price)
		plt.xlabel("km")
		plt.ylabel("price")
		plt.show()
		plt.scatter(km, price)

	min_km = min(km)
	max_km = max(km)
	diff_km = max_km - min_km
	min_price = min(price)
	diff_price = max(price) - min_price
	km = (km - min_km) / diff_km
	price = (price - min_price) / diff_price
	t0, t1 = train(km, price)
	save(t0, t1, min_km, max_km, min_price, diff_price)
	price1 = (min(km) * t1 + t0) * diff_price + min_price
	price2 = (max(km) * t1 + t0) * diff_price + min_price
	if ("-plot" in argv):
		plt.plot([min_km, max_km], [price1, price2], "red")
		plt.xlabel("km")
		plt.ylabel("price")
		plt.show()