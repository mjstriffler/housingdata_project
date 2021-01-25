# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle



app = Flask(__name__)



# Load the model
testrun = pickle.load(open('model.pkl','rb'))


##Define app routoe 
@app.route('/',methods=['POST'])



def predict():
    # Get the data from the POST request.
    #data = request.get_json(force=True)

    data = = pd.read_excel('2010-2019combineddata.xls')
    dummy = ["Year", "Before Tax Change", "Current residence in"]

    combined_data = pd.get_dummies(combined_data, columns= dummy)

    # Make prediction using model loaded from disk as per the data.
    prediction = testrun.predict([[np.array(combined_data['exp'])]])


    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

@app.route("/")
def tableau():
   
    return render_template("tableau.html")



if __name__ == '__main__':
    app.run(debug=True)