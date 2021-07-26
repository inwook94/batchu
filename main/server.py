from flask import Flask, render_template, request

import datetime


import numpy as np
import pickle
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
app = Flask(__name__,template_folder='templates')



pkl_filename = "./model/pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)



@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'GET':

        return render_template('full-img-cover.html')

    if request.method == 'POST':

        

        avg_temp = float(request.form['avg_temp'])

        min_temp = float(request.form['min_temp'])

        max_temp = float(request.form['max_temp'])

        rain_fall = float(request.form['rain_fall'])



        

        price = 0



        

        new = [[avg_temp,min_temp,max_temp,rain_fall]]





        


            
        

        

        price = pickle_model.predict(new)[0]



        return render_template('full-img-cover.html',price=price)



if __name__ == '__main__':

   app.run(debug = True)


