import csv
import json

def load_data_csv(filename):
	milage = []
	price = []
	try:
		with open(filename, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				milage.append(float(row["km"]))
				price.append(float(row['price']))
		return milage, price
	except FileNotFoundError:
		print("data.csv Was Not Found.")
		exit(1)

def estimated_price(milage, thet0, thet1):
	return thet0 + thet1 * milage

def train(milage, price, learning_rate = 0.01, epochs = 1000):
	m = len(milage)
	thet0 = 0.0
	thet1 = 0.0
	for epoch in range(epochs):
		sum_error = 0.0
		sum_error_milage = 0.0
		for i in range(m):
			estim_price = estimated_price(milage[i], thet0, thet1)
			error = estim_price - price[i]
			sum_error += error
			sum_error_milage += error * milage[i]

		tmp_thet0 = learning_rate * sum_error / m
		tmp_thet1 = learning_rate * sum_error_milage / m

		thet0 -= tmp_thet0
		thet1 -= tmp_thet1
	return thet0, thet1

def save_model(theta0, theta1, min_mileage, max_mileage, filename='model.json'):
	with open(filename, 'w') as f:
		json.dump({
			'theta0': theta0,
			'theta1': theta1,
			'min_mileage': min_mileage,
			'max_mileage': max_mileage
		}, f)


if __name__ == '__main__':
	milage, price = load_data_csv('data.csv')
	min_mileage = min(milage)
	max_mileage = max(milage)
	milage = [(x - min_mileage) / (max_mileage - min_mileage) for x in milage]
	theta0, theta1 = train(milage, price)
	save_model(theta0, theta1, min_mileage, max_mileage)
	print(f"model trained.")

