from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():

    hour = int(request.form['hour'])
    day = int(request.form['day'])
    weekend = int(request.form['weekend'])
    holiday = int(request.form['holiday'])

    features = np.array([[hour,day,weekend,holiday]])

    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Crowd Level: {prediction[0]}"
    )

if __name__ == "__main__":
    app.run(debug=True)