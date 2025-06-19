import json

def load_model(filename='model.json'):
	try:
		with open(filename, 'r') as f:
			model = json.load(f)
			return model['theta0'], model['theta1'], model['min_mileage'], model['max_mileage']
	except FileNotFoundError:
		print("Model has not been trained yet. Please run train.py first")
		exit(1)

def estimated_price(mileage, theta0, theta1, min_mileage, max_mileage):
	normalized = (mileage - min_mileage) / (max_mileage - min_mileage)
	return theta0 + theta1 * normalized

if __name__ == '__main__':
	theta0, theta1, min_mileage, max_mileage = load_model()
	try:
		print("⚠️ Warning: Inputing a mileage that is outside the range of training data might provide innacurate results.\n Range : 22899 to 240000.")
		mileage = float(input("Enter the mileage in Km : "))
		price = estimated_price(mileage, theta0, theta1, min_mileage, max_mileage)
		print(f"The estimated price is : {round(price, 2)}")
	except ValueError:
		print("Invalid input. Please enter a numeric value.")
