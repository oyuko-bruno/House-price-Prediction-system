from turtle import pd

import numpy as np
from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

def home(request):

    return render(request, 'home.html')
def predict(request):

    return render(request, 'predict.html')


def result(request):

    data = pd.read_csv(r'C:\Users\Administrator\anaconda3\Projects\Untitled Folder/USA_Housing.csv')
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']

    from sklearn.model_selection import train_test_split

    # Assuming data is your feature matrix and target is your target variable
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    #pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))

   # pred = round(pred = 0)

   # price = "The predicted price is $"+str(pred)
    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))[0]
    pred = round(pred, 2)

    price = "The predicted price is $" + str(pred)
    return render(request, 'predict.html', {"result2": price})





   # return render(request, 'predict.html',{"result2":price})