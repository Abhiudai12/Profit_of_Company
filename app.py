from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load("Reg_model.pkl")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        try:
            NewYork=float(request.form['NewYork'])
            California=float(request.form['California'])
            Florida=float(request.form['Florida'])
            Rndd_spend=float(request.form['Rndd_spend'])
            admin_spend=float(request.form['admin_spend'])
            market_spend=float(request.form['market_spend'])
            pred_args=[NewYork, California, Florida, Rndd_spend, admin_spend, market_spend]
            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)
            model_prediction=model.predict(pred_args_arr)
            model_prediction=round(float(model_prediction),2)
        except ValueError:
            model_prediction = "Invalid Input"
        return render_template('predict.html',prediction=model_prediction)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
