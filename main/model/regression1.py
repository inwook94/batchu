
from sklearn import datasets
import pickle
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
data = pd.read_csv('price data.csv', sep=',')
data
X=data[['avgTemp','minTemp','maxTemp','rainFall']]
y=data['avgPrice']



line_fitter = LinearRegression()
line_fitter.fit(X, y)
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(line_fitter, file)

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

new=[[-4.9,-11,-0.9,0]]

line_fitter.predict(new)

pickle_model.predict(new)
