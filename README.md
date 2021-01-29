# Influences of National Geographic Migration 
## Machine Learning Application

In order to deploy our app, please use the **deployApp.py** file to run the Flask app. This app is connects our model with our HTML pages that hold the form for the user-inputted variables and Tableau visualizations. 

Using our site, users can input certain variables and have our model predict the net migration for that state. It also provides our users with the visualizations of net migration across the United States for the past decade. Ultimately, we created an HTML webpage that runs through our Flask server that holds all our findings. Despite our limitations, we successfully produced interactive visualizations of our extracted results



**Data Analysis & Visualizations**

In this report, data from the U.S. Census Bureau ACS was obtained by extracting Excel files of state to state migration, median income, and unemployment rate over the past decade (from 2010-2019). In addition to this, state median home prices were obtained from Zillow Research hub. From here, data was cleaned by dropping unnecessary columns and adding in columns for the other data files. These files were then read through a Python jupyter notebook in order to append the different yearly datasets and combine into one comprehensive  dataset. Using this file, we tested different types of machine learning techniques to hypothesize if our model would have the ability to predict the migration from one state to another using the different variables listed above. Visualizations were then created using Tableau. Ultimately, a dashboard was created where the user could input certain state criteria to predict migration as well to display our predictive model and visualizations. 
