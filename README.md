# ft_linear_regression

A simple linear regression implementation from scratch to predict car prices based on mileage, built as part of the 42 School curriculum.

## Overview

This project implements a linear regression algorithm to predict car prices based on their mileage. The implementation is done from scratch without using machine learning libraries, focusing on understanding the fundamental concepts of linear regression.

## Features

- **Training**: Train a linear regression model using gradient descent
- **Prediction**: Predict car prices based on mileage input
- **Data Normalization**: Automatic feature scaling for better convergence
- **Model Persistence**: Save and load trained models using JSON

## Files Structure

```
ft_linear_regression/
├── data.csv        # Dataset containing car mileage and prices
├── train.py        # Training script for the linear regression model
├── predict.py      # Prediction script using the trained model
└── README.md       # This file
```

## Dataset

The dataset (`data.csv`) contains car data with two columns:
- `km`: Car mileage in kilometers
- `price`: Car price

The dataset includes 24 data points with mileage ranging from 22,899 to 240,000 km.

## Usage

### Training the Model

First, train the linear regression model using the provided dataset:

```bash
python3 train.py
```

This will:
- Load the data from `data.csv`
- Normalize the mileage data
- Train the model using gradient descent
- Save the trained model parameters to `model.json`

### Making Predictions

After training, you can predict car prices by running:

```bash
python3 predict.py
```

The script will:
- Load the trained model from `model.json`
- Prompt you to enter a car's mileage
- Return the estimated price

**Note**: The model works best for mileage values within the training range (22,899 to 240,000 km).

## Algorithm Details

### Linear Regression Formula
```
price = θ₀ + θ₁ × mileage
```

Where:
- `θ₀` (theta0): y-intercept
- `θ₁` (theta1): slope

### Training Process
1. **Data Normalization**: Mileage values are normalized to [0,1] range
2. **Gradient Descent**: Parameters are updated iteratively using:
   - Learning rate: 0.01
   - Epochs: 1000
3. **Cost Function**: Mean squared error minimization

## Example

```bash
$ python3 train.py
model trained.

$ python3 predict.py
⚠️ Warning: Inputing a mileage that is outside the range of training data might provide innacurate results.
 Range : 22899 to 240000.
Enter the mileage in Km : 100000
The estimated price is : 6417.85
```

## Requirements

- Python 3.x
- No external dependencies (uses only built-in libraries)

## Implementation Notes

- The implementation uses gradient descent optimization
- Feature scaling is applied to improve convergence
- Model parameters are saved in JSON format for persistence
- Input validation is included for robust error handling

## Educational Purpose

This project is designed for learning purposes to understand:
- Linear regression fundamentals
- Gradient descent optimization
- Feature normalization
- Model training and evaluation concepts

---

*This project is part of the 42 School curriculum focusing on machine learning fundamentals.* 