# main.py (Flask app)
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and pipeline
model = joblib.load("training/model.pkl")
pipeline = joblib.load("training/pipeline.pkl")

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Form data from user
            input_data = {
                'longitude': float(request.form['longitude']),
                'latitude': float(request.form['latitude']),
                'housing_median_age': float(request.form['housing_median_age']),
                'total_rooms': float(request.form['total_rooms']),
                'total_bedrooms': float(request.form['total_bedrooms']),
                'population': float(request.form['population']),
                'households': float(request.form['households']),
                'median_income': float(request.form['median_income']),
                'ocean_proximity': request.form['ocean_proximity']
            }

            df = pd.DataFrame([input_data])
            transformed = pipeline.transform(df)
            prediction = model.predict(transformed)[0]

            return render_template("index.html", prediction=round(prediction, 2))
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {e}")

    return render_template("index.html", prediction=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

