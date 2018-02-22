# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)'''

# Simple Linear Regression fit  (training model)
from sklearn.linear_model import LinearRegression
myRegressor = LinearRegression()
myRegressor.fit(X_train, y_train)   #fitting linearRegresion model to train data

# Prediciting results on test set (testing trained model)
y_pred = myRegressor.predict(X_test) #y_pred - predicated salaries 

# Visualizing the train data - pretty starighforward
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train,  myRegressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience [trainingSet]')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the test data
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train,  myRegressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience [testSet]')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()