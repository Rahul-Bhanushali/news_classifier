from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('nb.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        test_text =  request.form.getlist('test_text[]')
        prediction=model.predict(test_text)
        output=prediction[0]
    return render_template('index.html',prediction_text="News classified as:{}".format(output))

if __name__=="__main__":
    app.run(debug=True)
