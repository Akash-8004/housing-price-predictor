# 🏡 House Price Predictor - Machine Learning Flask App

A machine learning project that predicts house prices using a trained Random Forest model on the California housing dataset. The project includes a web interface built using Flask, where users can input housing data and receive real-time predictions.

---

## 🚀 Demo

Live app hosted on [Render](https://your-render-link-here) *(replace this with your actual link after deployment)*

---

## 📁 Project Structure



housing-price-predictor/
│
├── static/ # Contains CSS stylesheets
│ └── style.css
│
├── templates/ # HTML templates for Flask app
│ └── index.html
│
├── model.pkl # Trained RandomForestRegressor model
├── pipeline.pkl # Preprocessing pipeline (imputer, scaler, encoder)
├── app.py # Flask web app to serve model predictions
├── train_model.py # Script to train the model
├── requirements.txt # Python dependencies
├── README.md # Project documentation



---

## 💡 Features

- 📊 Trained on the California Housing Dataset
- 🔧 Preprocessing using pipelines (handling NA values, scaling, encoding)
- 🌐 Flask-based web interface
- 🧠 Random Forest Regression model
- 📈 Outputs predicted `median_house_value` based on input features
- 🎨 Styled using external CSS

---

## 📦 Setup Instructions

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/housing-price-predictor.git
cd housing-price-predictor

✅ Step 2: Install Dependencies
pip install -r requirements.txt

✅ Step 3: Train the Model (Optional)
If you want to retrain the model:

python train_model.py
This will create model.pkl and pipeline.pkl.

✅ Step 4: Run the Flask App
python app.py
Visit http://localhost:5000 in your browser.


🌐 Deployment (Render)
📄 Create render.yaml

services:
  - type: web
    name: house-price-predictor
    env: python
    buildCommand: ""
    startCommand: python app.py
    plan: free
📋 Add requirements.txt

Flask
pandas
scikit-learn
joblib
🚀 Deploy
Push your code to GitHub.

Create a free Render account: https://render.com

Click "New Web Service" and connect your GitHub repo.

Configure as:

Build Command: ()

Start Command: python app.py

Environment: Python

Deploy!

📘 Technologies Used
Python

Pandas, NumPy

Scikit-learn

Flask

HTML5, CSS3

Render (for hosting)

🧠 Skills Demonstrated
Supervised ML (Regression)

Data Cleaning & Feature Engineering

One-Hot Encoding, Standardization

Scikit-learn Pipelines & Transformers

Model Deployment (Flask + Render)

Git & GitHub project structuring



✍️ Author
Akash
GitHubhttps://github.com/Akash-8004 | https://www.linkedin.com/in/akash-yadav-284909321/

📄 License
MIT License – free to use and modify.


---

Let me know if you'd like me to create this file and let you download it directly as `README.md`, or help push to GitHub.