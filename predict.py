if __name__ == "__main__":
	try:
		km = float(input("enter a mileage: "))
		if (km <= 0):
			raise Exception
	except:
		print("incorrect value")
		exit(-1)
	try:
		with open("./values", 'r') as file:
			a = float(file.readline())
			b = float(file.readline())
	except:
		a = 0.0
		b = 0.0
	price = a * km + b
	if (price < 0):
		price = 0
	print("car value:", int(price))