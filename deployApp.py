# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from tensorflow.keras.models import load_model
import joblib


app = Flask(__name__)



# Load the model

with open('model.pkl', 'rb') as file:  
    testrun = pickle.load(file)

#testrun = pickle.load(open('model.pkl','rb'))
# testrun = load_model("migration_trained.h5")

##Define app routoe 
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':

        medincome = request.form['Median Income']
        homeprice = request.form['Avg Home Price']
        umemployment = request.form["Unemployment Rate"]
        totalpop = request.form["Total Population"]
        usState = request.form['State']
        statekey = "Current residence in_" + usState
        
        dict = {"Median Income" : int(medincome), "Avg Home Price" : int(homeprice), "Unemployment Rate": int(umemployment), statekey: "1"}
        data = list(dict.items())
        predMigrate = testrun.predict(np.array(data))

        return render_template('tableau.html', predMigrate=predMigrate)

    return render_template('tableau.html')
    
     
# let data = {element: "barium"};
# fetch("/post/data/here", {
#   method: "POST", zåß
#   body: JSON.stringify(data)
# }).then(res => {
#   console.log("Request complete! response:", res);
# })

# def predict():
#     # Get the data from the POST request.
#     data = request.get_json(force=True)

#     data = pd.read_excel('2010-2019combineddata.xls')
#     dummy = ["Year", "Before Tax Change", "Current residence in"]

#     combined_data = pd.get_dummies(data, columns= dummy)

#     # Make prediction using model loaded from disk as per the data.
#     prediction = testrun.predict(np.array

#  pred = model.predict(np.array([int(bedrooms), int(baths), int(sqft]))
#     # Take the first value of prediction
#     output = prediction[0]
#     return jsonify(output)

#     return render_template("tableau.html")


# @app.route("/")
# def tableau():
   
#     return render_template("tableau.html")



if __name__ == '__main__':
    app.run(debug=True)