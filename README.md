# DataMining    
For the .ipynb files, please open in Google colab and run all the cells to see the results.

## Instructions for the Decision Tree and Multinomial Naive Bayes models
The code for the Decision Tree is provided in the Python file name "Decision_Tree.ipynb".
The code for the Multinomial Naive Bayes model is provided in the Python file name "Multinomial_Naive_Bayes.ipynb".
The code for each model can be run on the training set directly, after which an output of the models accuracy on the training data will be shown. To run each model on the testing data, uncomment the code indicated at the end of each file. The code to uncomment is the following lines

`testingX2 = pd.read_csv('/content/testing.csv', sep=',')`

`predictionY2 = clf.predict(testingX2)`

`for value in predictionY2:`

`print(value)`

Once these commands are uncommented, the models will begin predicting values for the testing set. An output of each prediction will be displayed once the code is run.
