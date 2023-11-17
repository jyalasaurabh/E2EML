import os
import sys
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

app = application

# Routr for a home page


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            lunch=request.form.get("lunch"),
            parental_level_education=request.form.get(
                "parental_level_of_education"),
            race_ethnicity=request.form.get("ethnicity"),
            reading_score=request.form.get("reading_score"),
            test_prep_course=request.form.get("test_preparation_course"),
            writing_score=request.form.get("writing_score")
        )
        pred_df = data.getDataFrame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print(results)
        return render_template("home.html", result=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
