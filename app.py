# Import libraries
from flask import Flask, render_template, jsonify
import numpy as np
import requests
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



app = Flask(__name__)



# Load the model
testrun = pickle.load(open('model.pkl','rb'))


##Define app routoe 
@app.route('/',methods=['GET','POST'])



def predict():
    # Get the data from the POST request.
    #data = requests.get_json(force=True)
    # columns = ['Median Income', 'Avg. Home Price','Unemployment Rate','Total Population','Year_2010',
    #     'Year_2011',
    #     'Year_2012',
    #     'Year_2013',
    #     'Year_2014',
    #     'Year_2015',
    #     'Year_2016',
    #     'Year_2017',
    #     'Year_2018',
    #     'Year_2019',
    #     'Before Tax Change_no','Before Tax Change_yes',
    #     'Current residence in_Alabama',
    #     'Current residence in_Alaska',
    #     'Current residence in_Arizona',
    #     'Current residence in_Arkansas',
    #     'Current residence in_California',
    #     'Current residence in_Colorado',
    #     'Current residence in_Connecticut',
    #     'Current residence in_Delaware',
    #     'Current residence in_District of Columbia ',
    #     'Current residence in_Florida',
    #     'Current residence in_Georgia',
    #     'Current residence in_Hawaii',
    #     'Current residence in_Idaho',
    #     'Current residence in_Illinois',
    #     'Current residence in_Indiana',
    #     'Current residence in_Iowa',
    #     'Current residence in_Kansas',
    #     'Current residence in_Kentucky',
    #     'Current residence in_Louisiana',
    #     'Current residence in_Maine',
    #     'Current residence in_Maryland',
    #     'Current residence in_Massachusetts',
    #     'Current residence in_Michigan',
    #     'Current residence in_Minnesota',
    #     'Current residence in_Mississippi',
    #     'Current residence in_Missouri',
    #     'Current residence in_Montana',
    #     'Current residence in_Nebraska',
    #     'Current residence in_Nevada',
    #     'Current residence in_New Hampshire',
    #     'Current residence in_New Jersey',
    #     'Current residence in_New Mexico',
    #     'Current residence in_New York',
    #     'Current residence in_North Carolina',
    #     'Current residence in_North Dakota',
    #     'Current residence in_Ohio',
    #     'Current residence in_Oklahoma',
    #     'Current residence in_Oregon',
    #     'Current residence in_Pennsylvania',
    #     'Current residence in_Rhode Island',
    #     'Current residence in_South Carolina',
    #     'Current residence in_South Dakota',
    #     'Current residence in_Tennessee',
    #     'Current residence in_Texas',
    #     'Current residence in_Utah',
    #     'Current residence in_Vermont',
    #     'Current residence in_Virginia',
    #     'Current residence in_Washington',
    #     'Current residence in_West Virginia',
    #     'Current residence in_Wisconsin',
    #     'Current residence in_Wyoming']
    combined_data = pd.read_excel('2010-2019combineddata.xls')
    dummy = ["Year", "Before Tax Change", "Current residence in"]
    combined_data = pd.get_dummies(combined_data, columns= dummy)
    
    #X = combined_data[columns].values
    #y = combined_data["Net Migration"].values.reshape(-1, 1)

    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    # model = LinearRegression()
    # model.fit(X_train, y_train)
    # predicted = model.predict(X_test)

    # Make prediction using model loaded from disk as per the data.
    prediction = testrun.predict([[np.array(combined_data[columns])]])


    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

#@app.route("/")
#def tableau():
   
 #   return render_template("tableau.html")



if __name__ == '__main__':
    app.run(debug=True)