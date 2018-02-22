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

# 4. Categorical data encoding 
''' 
We want to have a numercial labels attatched to categories with text values
'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_featuresMatrix = LabelEncoder()
featuresMatrix[:, 0] = labelEncoder_featuresMatrix.fit_transform\
(featuresMatrix[:, 0])
#the line above returns encoded values of first column of matrix featuresMatrix

#Now Dummy Encoding
'''
Sometimes we dont want to have different numerical values for a category,
for example category "country" shouldnt be rated in 0-x scale, because having
higher values for different countries doesnt make any sense. Dummy encoding
transforms a single category into several categories for every unique input and
rates it 0-1 (is/isn't)
'''
oneHotEnc = OneHotEncoder(categorical_features=[0])
featuresMatrix = oneHotEnc.fit_transform(featuresMatrix).toarray()

#Now label encoding of dependant variables
''' The same as for #4'''
labelEncoder_dependentVariable = LabelEncoder()
dependentVariables=labelEncoder_dependentVariable.fit_transform(dependentVariables)

#Dividing into test and training sets
from sklearn.cross_validation import train_test_split
featuresTrain, featuresTest, resultsTrain, resultsTest = \
train_test_split(featuresMatrix, dependentVariables, test_size = 0.2,\
                 random_state = 0)

#Feature scaling (well that pretty obvious why you have to do it)
from sklearn.preprocessing import StandardScaler
scaledFeatures = StandardScaler()
featuresTrain = scaledFeatures.fit_transform(featuresTrain)
featuresTest = scaledFeatures.transform(featuresTest)










