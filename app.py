# app.py
import os
from flask import Flask, request, jsonify
from db import init_db
from model import WeatherModel

# Initialize DB
init_db()

# Load + Train model
weather_model = WeatherModel()
weather_model.train()

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "Weather Prediction API running"}

@app.route("/predict", methods=["GET"])
def predict():
    temp = request.args.get("temp", type=float)
    if temp is None:
        return jsonify({"error": "Missing ?temp=xx"}), 400
    
    prediction = weather_model.predict(temp)
    result = "Sunny" if prediction == 1 else "Not Sunny"

    return jsonify({
        "temperature": temp,
        "prediction": result
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # required by Render
    app.run(host="0.0.0.0", port=port)
