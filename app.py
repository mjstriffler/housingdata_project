from flask import Flask, render_template, redirect
from sql_keys import username, password
from sqlalchemy import create_engine
import requests


# Create an instance of Flask
app = Flask(__name__)


# Create engine connection
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/satellite')

# App Route for Home Page
@app.route("/")
def home():

    # 
    country = engine.execute("select * from country ", con=engine)
    data_cat = engine.execute("select * from satellite_category", con=engine)
    sat_ids = engine.execute("select satellite_id from country_satellite order by 1", con=engine)
    sat_names = engine.execute("select satellite_name from country_satellite order by 1", con=engine)
    # Return template and data
  
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("index.html", country=country, category=data_cat, responsedata=responsedata, 
            init_page="initpage", sat_ids=sat_ids, sat_names=sat_names)



# App Route for selected satellite(s) based on country and satellite number 
@app.route("/getSatellite/<cntry>/<numSat>")
def satellite_country(cntry,numSat):

    # 
    sat_cnt_cnt = engine.execute("select * from country_satellite where country_code='"+cntry+"'", con=engine)
    country = engine.execute("select * from country ", con=engine)
    data_cat = engine.execute("select * from satellite_category", con=engine)
    sat_ids = engine.execute("select satellite_id from country_satellite order by 1", con=engine)
    sat_names = engine.execute("select satellite_name from country_satellite order by 1", con=engine)
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
            print(url)

            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
            
      
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1
        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,
     init_page="notinitpage" , sat_ids=sat_ids, sat_names=sat_names, sel_cnt=cntry)

# App route for satellites(s) by ID number
@app.route("/getSatelliteById/<satid>/<numSat>")
def satellite_byid(satid,numSat):

    #
    sat_cnt_cnt = engine.execute("select * from country_satellite where satellite_id='"+satid+"'", con=engine)
    country = engine.execute("select * from country ", con=engine)
    data_cat = engine.execute("select * from satellite_category", con=engine)
    sat_ids = engine.execute("select satellite_id from country_satellite order by 1", con=engine)
    sat_names = engine.execute("select satellite_name from country_satellite order by 1", con=engine)
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
          
            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
        
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1
        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,  
    init_page="notinitpage" , sat_ids=sat_ids, sat_names=sat_names, sat_sel_id=satid)

# App route for satellites(s) by satellite name
@app.route("/getSatelliteByName/<satName>/<numSat>")
def satellite_byname(satName,numSat):

    # 
    sat_cnt_cnt = engine.execute("select * from country_satellite where satellite_name='"+satName+"'", con=engine)
    country = engine.execute("select * from country ", con=engine)
    data_cat = engine.execute("select * from satellite_category", con=engine)
    sat_ids = engine.execute("select satellite_id from country_satellite order by 1", con=engine)
    sat_names = engine.execute("select satellite_name from country_satellite order by 1", con=engine)
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
        
            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
   
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1
        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,
      init_page="notinitpage", sat_ids=sat_ids, sat_names=sat_names,sel_name=satName)


# Route to satellite chart and altitude map
@app.route("/indexplots")
def indexplots():
   
    return render_template("index_plots.html")


# Route to Earth Resources satellites map
@app.route("/minimapindex")
def minimapindex():
   
    return render_template("minimap_index.html")


# Route to Earth Resources satellites on 3D globe
@app.route("/satglobe")
def satglobe():

    return render_template("satGlobe.html")


# Route to satellite launch sites cluster map
@app.route("/cluster")
def cluster():
   
    return render_template("cluster.html")

if __name__ == "__main__":
    app.run(debug=True)






# # Import libraries
# from flask import Flask, render_template, jsonify
# import numpy as np
# import requests
# import pickle
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression



# app = Flask(__name__)



# # Load the model
# testrun = pickle.load(open('model.pkl','rb'))


# ##Define app routoe 
# @app.route('/',methods=['GET','POST'])



# def predict():
#     # Get the data from the POST request.
#     #data = requests.get_json(force=True)
#     # columns = ['Median Income', 'Avg. Home Price','Unemployment Rate','Total Population','Year_2010',
#     #     'Year_2011',
#     #     'Year_2012',
#     #     'Year_2013',
#     #     'Year_2014',
#     #     'Year_2015',
#     #     'Year_2016',
#     #     'Year_2017',
#     #     'Year_2018',
#     #     'Year_2019',
#     #     'Before Tax Change_no','Before Tax Change_yes',
#     #     'Current residence in_Alabama',
#     #     'Current residence in_Alaska',
#     #     'Current residence in_Arizona',
#     #     'Current residence in_Arkansas',
#     #     'Current residence in_California',
#     #     'Current residence in_Colorado',
#     #     'Current residence in_Connecticut',
#     #     'Current residence in_Delaware',
#     #     'Current residence in_District of Columbia ',
#     #     'Current residence in_Florida',
#     #     'Current residence in_Georgia',
#     #     'Current residence in_Hawaii',
#     #     'Current residence in_Idaho',
#     #     'Current residence in_Illinois',
#     #     'Current residence in_Indiana',
#     #     'Current residence in_Iowa',
#     #     'Current residence in_Kansas',
#     #     'Current residence in_Kentucky',
#     #     'Current residence in_Louisiana',
#     #     'Current residence in_Maine',
#     #     'Current residence in_Maryland',
#     #     'Current residence in_Massachusetts',
#     #     'Current residence in_Michigan',
#     #     'Current residence in_Minnesota',
#     #     'Current residence in_Mississippi',
#     #     'Current residence in_Missouri',
#     #     'Current residence in_Montana',
#     #     'Current residence in_Nebraska',
#     #     'Current residence in_Nevada',
#     #     'Current residence in_New Hampshire',
#     #     'Current residence in_New Jersey',
#     #     'Current residence in_New Mexico',
#     #     'Current residence in_New York',
#     #     'Current residence in_North Carolina',
#     #     'Current residence in_North Dakota',
#     #     'Current residence in_Ohio',
#     #     'Current residence in_Oklahoma',
#     #     'Current residence in_Oregon',
#     #     'Current residence in_Pennsylvania',
#     #     'Current residence in_Rhode Island',
#     #     'Current residence in_South Carolina',
#     #     'Current residence in_South Dakota',
#     #     'Current residence in_Tennessee',
#     #     'Current residence in_Texas',
#     #     'Current residence in_Utah',
#     #     'Current residence in_Vermont',
#     #     'Current residence in_Virginia',
#     #     'Current residence in_Washington',
#     #     'Current residence in_West Virginia',
#     #     'Current residence in_Wisconsin',
#     #     'Current residence in_Wyoming']
#     combined_data = pd.read_excel('2010-2019combineddata.xls')
#     dummy = ["Year", "Before Tax Change", "Current residence in"]
#     combined_data = pd.get_dummies(combined_data, columns= dummy)
    
#     #X = combined_data[columns].values
#     #y = combined_data["Net Migration"].values.reshape(-1, 1)

#     # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
#     # model = LinearRegression()
#     # model.fit(X_train, y_train)
#     # predicted = model.predict(X_test)

#     # Make prediction using model loaded from disk as per the data.
#     prediction = testrun.predict([[np.array(combined_data[columns])]])


#     # Take the first value of prediction
#     output = prediction[0]
#     return jsonify(output)

# #@app.route("/")
# #def tableau():
   
#  #   return render_template("tableau.html")



# if __name__ == '__main__':
#     app.run(debug=True)