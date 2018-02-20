# Data Preprocessing

# 1. - importing the libraries
'''
numpy - math operations
matplot - plots
pandas - importing datasets
'''
import numpy as np     
import matplotlib.pyplot as plot
import pandas as pnd

# 2. importing data set
testDataset = pnd.read_csv('Data.csv')
featuresMatrix = testDataset.iloc[:, :-1].values#   features
dependentVariables = testDataset.iloc[:, 3].values# class

# 3. missing data problem
# 1. replacing NaNs with mean of the feature
from sklearn.preprocessing import Imputer
imputer = Imputer('NaN', 'mean',0)
#for NaN replace with mean calculated for column
imputer = imputer.fit(featuresMatrix[:, 1:3])   
featuresMatrix[:, 1:3] = imputer.transform(featuresMatrix[:, 1:3])
# What we did was that we used an object of class imputer, send him the data
# to be filled, told him how to do it and got our missing data replaced with
# the mean of the feature