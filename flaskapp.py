# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd



app = Flask(__name__)



# Load the model
testrun = pickle.load(open('model.pkl','rb'))


##Define app routoe 
@app.route('/')



def predict():
    # Get the data from the POST request.
    #data = request.get_json(force=True)

    data = pd.read_excel('2010-2019combineddata.xls')
    dummy = ["Year", "Before Tax Change", "Current residence in"]

    combined_data = pd.get_dummies(data, columns= dummy)

    # Make prediction using model loaded from disk as per the data.
    prediction = testrun.predict([[np.array(combined_data['Net Migration'])]])


    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

    return render_template(jsonify(output))


@app.route("/")
def tableau():
   
    return render_template("tableau.html")



if __name__ == '__main__':
    app.run(debug=True)