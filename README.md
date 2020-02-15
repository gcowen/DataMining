# DataMining    
For the .ipynb files, please open in Google colab and run all the cells to see the results.     
Best Model: SVM      

## Instructions for the Support Vector Machine and K-Nearest Neighbours models      
The KNN_and_SVM.ipynb includes all the codes and results of these two models.     
To generate SVM_prediction.csv, please run generate_SVM_pred.py and change the path of testing data accordingly.    
To generate KNN_prediction.csv, please run generate_KNN_pred.py and change the path of testing data accordingly.    

## Instructions for the Decision Tree and Multinomial Naive Bayes models
The code for the Decision Tree is provided in the Python file name "Decision_Tree.ipynb".
The code for the Multinomial Naive Bayes model is provided in the Python file name "Multinomial_Naive_Bayes.ipynb".
The code for each model can be run on the training set directly, after which an output of the models accuracy on the training data will be shown. To run each model on the testing data, upload the testing.csv to Google Colab and uncomment the code indicated at the end of each file. The code to uncomment is the following lines

`testingX2 = pd.read_csv('./DataMining/testing.csv', sep=',')`

`predictionY2 = clf.predict(testingX2)`

`for value in predictionY2:`

`print(value)`

Once these commands are uncommented, the models will begin predicting values for the testing set. If the code doesn't run because of an incorrect path, then copy paste the testing.csv file path onto ./DataMining/testing.csv. An output of each prediction will be displayed once the code is correctly run.

## Instructions for the Neural Network and Random Forest models
 Please run `TESTFORNeuralNetworkandRandomforesr.py` to see the testing result,  still need to copy the true label in the same path and change a revise of the code. (see the instruction inside the file)<br>
 The code for  Neural Network and Random Forest models is provided in the Python file name `"NeuralNetworkandRandomForest.ipynp"`.<br>
 The trained model are name as `MLP.pkl` and `RFC.pkl` which are already used in `TESTFORNeuralNetworkandRandomforesr.py`.<br><br>
 As the prediction results are not fully printed, please check the generated prediction result  named as `Y_predictMLP.csv` and `Y_predictRFC.csv`.
 <br>
 
 Please check `"NeuralNetworkandRandomForest.ipynp"`first then using the true label and run `TESTFORNeuralNetworkandRandomforesr.py`to see final accuracy.
 <br><br>
