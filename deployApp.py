# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from tensorflow.keras.models import load_model
import joblib


app = Flask(__name__)


# Load the model

with open('predict.pkl', 'rb') as file:  
    testrun = pickle.load(file)

#testrun = pickle.load(open('model.pkl','rb'))
# testrun = load_model("migration_trained.h5")

##Define app routoe 
@app.route('/', methods=['GET', 'POST'])



def index():
    if request.method == 'POST':

     

        medincome = (request.form['Median Income'])
        homeprice = request.form.get('Avg Home Price')
        umemployment = request.form.get("Unemployment Rate")
        totalpop = request.form.get("Total Population")
         

# stateList = [
#         Alabama,
#         Alaska,
#         Arizona,
#         Arkansas,
#         California,
#         Colorado,
#         Connecticut,
#         Delaware,
#         Florida,
#         Georgia,
#         Hawaii,
#         Idaho,
#         Illinois,
#         Indiana,
#         Iowa,
#         Kansas,
#         Kentucky,
#         Louisiana,
#         Maine,
#         Maryland,
#         Massachusetts,
#         Michigan,
#         Minnesota,
#         Mississippi,
#         Missouri,
#         Montana,
#         Nebraska,
#         Nevada,
#         New_Hampshire,
#         New_Jersey,
#         New_Mexico,
#         New_York,
#         North_Carolina,
#         North_Dakota,
#         Ohio,
#         Oklahoma,
#         Oregon,
#         Pennsylvania,
#         Rhode_Island,
#         South_Carolina,
#         South_Dakota,
#         Tennessee,
#         Texas,
#         Utah,
#         Vermont,
#         Virginia,
#         Washington,
#         West_Virginia,
#         Wisconsin,
#         Wyoming]

    # for state in stateList:

#         if  state == request.form["State"]:
            
#             statekey = "Current residence in_" + state


#         else:
#             nonstatekey = "Current residence in_" + state
    


        
        x1= {"Median Income" : [medincome], "Avg Home Price" : [homeprice], "Unemployment Rate": [umemployment], "Total Population" : [totalpop]}
        x2 = pd.DataFrame(x1)

        # data = list(dict.items())
        # data2 = np.array(data)
        # data3 = data2.tostring()
        # data4 = np.fromstring(data2, dtype=int)
        # usmig = [medincome, homeprice, umemployment, totalpop]

        predMigrate = testrun.predict(x2).reshape(-1,1)

        return render_template('tableau.html', predMigrate= predMigrate)

    return render_template('tableau.html')
    
     
# let data = {element: "barium"};
# fetch("/post/data/here", {
#   method: "POST", zåß
#   body: JSON.stringify(data)
# }).then(res => {
#   console.log("Request complete! response:", res);
# })

@app.route('/about')

def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)