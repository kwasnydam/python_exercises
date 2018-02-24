# -*- coding: utf-8 -*-
"""
@Topic: Multiple Linear Regression
@author: Damian Kwasny
This is a multiple linear regression example script. This time around we have a
number of independent variables and we need to build a model of how does the
single dependent variable depends upon all of them, which parameters are 
insignificant and all like that
5 approaches to building a model:
    1. All-in - using all vaiarbles:
        - Prior knowledge about the variables
        - You have to use all of them
        - Preparing for backward elimination
    2. Backward Elimination:
        Step1 - Select a significance level to stay in the model(ie sl =  0.05)
        Step2 - Fit the model with all variables
        Step3 - Take the predictor with the highest p-val, if p>sl: step4
                else: Final
        Step4 - Remove this variable
        Step5 - Fit model without this variable and go to Step3
        Final - Your model is ready
    3. Forward Selection:
        Step1 - Select a significance level to enter in the model(ie sl =  0.05)
        Step2 - Fit all simple regresion models (y~xn), select model with lowest pval
        Step3 - Keep this variable and we fit all models with one extra param
                in addition to the one we already have
        Step4 - Consider the predictor with lowest p-val, if p<SL: Step 3, else:Fin
        Final - every other variable is insignificant
    4. Bidirectional Elimination
    5. All possible models:
        Step1 - Select a criterion of quality
        Step2 - construct all possible models (2^N-1)
        Step3 - choose the one with the best quality criterion value
"""

# Data Preprocessing 

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data and creating dummy variables
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
#labelencoder_y = LabelEncoder()
#y = labelencoder_y.fit_transform(y)

# Avoiding the dummy variable trap:
X = X[:, 1:] # You have to remove one dummy variable (redundant dependency)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = y_train.reshape(-1,1)
y_train = sc_y.fit_transform(y_train)

# Fitting Multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
myRegressor = LinearRegression()
myRegressor.fit(X_train, y_train)

# Prediciting test results
y_pred = myRegressor.predict(X_test)

# Is the model we have gotten the optimal one? How do we determine that?

# Let's try a backward elimination technique
import statsmodels.formula.api as sm
values1 = np.ones((np.size(X[:,1]), 1))
X = np.append(arr = values1.astype(int), values = X, axis = 1)#x0 for b0x0
X_optimal = X

# backward elimination workflow
sl = 0.05 #step1: siginificance level
regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit() #step2. fitting all
bad_indices = set()
#while predictor_p_value > sl:
while True: 
    '''So what is going on here anyway?
    Basically, I store the column of p-values of my current model's predictors 
    in the summ variable as a list (I obtain it from the regresso_OLS.summary() object
    and it is not very pretty formula). Next I obtain the maximum p-val and it's index
    in predictor_p_value and predictor_p_index. If the p_value in this step is 
    higher then threshold sl, I remove it(it means it is insiginificant), else
    I am leaving the loop beacuse it means that all reamining var are siginificant.
    Removing the bad predictor is achieved by assigning a new X_optimal without
    the bad predictor column (which is removed in indices.remove part). Next I 
    create a new model and repeat the steps (step3-4 of backward elimination are
    described in here)
    '''
    summ = []
    summ = [regressor_OLS.summary().tables[1][i][4].data for i in range(1, np.size(regressor_OLS.summary().tables[1],0))]
    predictor_p_value, predictor_p_index = max(summ),  np.argmax(summ)
    if float(predictor_p_value) < sl: 
        break
    #bad_indices.add(predictor_p_index)
    #indices = [i for i in range(len(X[1,:]))]
    #for bad_index in bad_indices:
    indices = [i for i in range(len(X_optimal[1,:]))]
    indices.remove(predictor_p_index)
    X_optimal = X_optimal[:,indices]    
    regressor_OLS = sm.OLS(endog = y, exog = X_optimal).fit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    