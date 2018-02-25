# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
'''from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)'''

# Linear regression fitting:
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X, y)

# Fitting Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
polyReg = PolynomialFeatures(degree=4)
X_poly = polyReg.fit_transform(X)
polynomialRegressor = LinearRegression()
polynomialRegressor.fit(X_poly, y)

# Visualizing linearRegression results:
plt.scatter(X, y, color = 'red')
plt.plot(X, linearRegressor.predict(X))
plt.title('Truth or not the truth')

# Visualizing polynomialRegression results:
plt.plot(X, polynomialRegressor.predict(polyReg.fit_transform(X)), color = 'black')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.figlegend('Linear Regression','Polynomial Regression')

# Final prediction - predicting salary with the functions we have aquired
linearRegressor.predict(6.5)
polynomialRegressor.predict(polyReg.fit_transform(6.5))