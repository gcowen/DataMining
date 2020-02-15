# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:32:07 2020

@author: dell
"""
import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


train = pd.read_csv('C:/Users/dell/Desktop/Data mining/training.csv')
lab_encoder = LabelEncoder()
label = train['label']
label_encoded = lab_encoder.fit_transform(label)
label_encoded
df2 = train.drop(columns = ['label'])
x_train = df2.values
# split the training data set 
x_test = x_train[15000:21000] # use 1/3 of training data to test
x_train =x_train[0:14999] # use 2/3 of traing data to train 

from sklearn.preprocessing import MinMaxScaler #use this to do the scaling
scaling = MinMaxScaler(feature_range=(-1,1)).fit(x_train)
x_train = scaling.transform(x_train)
x_test = scaling.transform(x_test)

# svc classifier
model=svm.SVC()
model.fit(x_train,label_encoded[0:14999])
# compare = []
# for i in range(0,6000):
#    result = model.predict(x_test[i].reshape(1, 784))
#    compare.append(result[0]) 
# accuracy_score(compare, label[15000:21000])
test = pd.read_csv('C:/Users/dell/Desktop/Data mining/testing.csv')
test = scaling.transform(test)
predict=model.predict(test)
prediction = pd.DataFrame(predict, columns=['predictions']).to_csv('SVM_prediction.csv',index=False)