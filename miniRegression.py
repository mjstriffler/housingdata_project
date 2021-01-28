#Import dependancies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import requests
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


combined_data = pd.read_excel('2010-2019combineddata.xls')
dummy = ["Year", "Before Tax Change", "Current residence in"]

# combined_data = pd.get_dummies(combined_data, columns= dummy)

columns = ['Median Income', 'Avg Home Price','Unemployment Rate','Total Population',]

X = combined_data[columns].values
y = combined_data["Net Migration"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LinearRegression()

model.fit(X_train, y_train)


importance=model.coef_[0]

features_importance = []

for i, v in enumerate(importance):
    features_importance.append(v)


features_importance_names = zip(features_importance, columns)
print(tuple(features_importance_names))   

predicted = model.predict(X_test)

mse = mean_squared_error(y_test, predicted)
r2 = r2_score(y_test, predicted)

print('r-squared: ', r2)
print('y-axis intercept: ', model.intercept_)

pickle.dump(model, open('predict.pkl','wb'))

newrun = pickle.load(open('predict.pkl','rb'))
#testrun = pickle.load(open('model.pkl','rb'))
