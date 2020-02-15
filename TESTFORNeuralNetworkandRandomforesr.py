from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
import csv

def loadtest():
    tmp = np.loadtxt("testing.csv", dtype=np.str, delimiter=",")
    data = tmp[1:,0:].astype(np.float)
    return data
def loadtruelabel():
    truelabel=np.loadtxt("please in put the path of true label", dtype=np.str, delimiter=",")  ################################################
    return truelabel

theMLP = joblib.load('MLP.pkl')
theRFC = joblib.load('RFC.pkl')
TEST=loadtest()
MLP_label = theMLP.predict(TEST)
RFC_Label = theRFC.predict(TEST)
print(MLP_label)
print(RFC_Label)
#Y_true=loadtruelabel()                                                                 #######  DELETE the "#" to show final accuracy
#print("Accuracy of MLP:", metrics.accuracy_score(Y_true, MLP_label))                   #######  DELETE the "#" to show final accuracy
#print("Accuracy of RFCP:", metrics.accuracy_score(Y_true, RFC_Label))                  #######  DELETE the "#" to show final accuracy