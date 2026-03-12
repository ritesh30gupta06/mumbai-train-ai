# AI-Based Mumbai Local Train Crowd & Delay Predictor

This project predicts the crowd density in Mumbai local trains using Machine Learning.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask

## Features
- Predict crowd level (Low / Medium / High)
- Based on time, weekday, and holidays
- Simple web interface

## Project Structure
mumbai-train-ai
│
├── data
├── model
├── templates
├── app.py
├── model.pkl
├── requirements.txt
└── README.md

## How to Run

Install libraries

pip install -r requirements.txt

Train the model

python model/train_model.py

Run the web app

python app.py

Open browser

http://127.0.0.1:5000
