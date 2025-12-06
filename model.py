# model.py
import sqlite3
import numpy as np
from sklearn.linear_model import LinearRegression

class WeatherModel:
    def __init__(self):
        self.model = LinearRegression()

    def load_data(self):
        conn = sqlite3.connect("weather.db")
        cur = conn.cursor()
        cur.execute("SELECT temperature, sunny FROM weather")
        data = cur.fetchall()
        conn.close()

        data = np.array(data)
        X = data[:, 0].reshape(-1, 1)   
        y = data[:, 1]                 
        return X, y

    def train(self):
        X, y = self.load_data()
        self.model.fit(X, y)

    def predict(self, temp):
        pred = self.model.predict([[temp]])[0]
        return 1 if pred >= 0.5 else 0
