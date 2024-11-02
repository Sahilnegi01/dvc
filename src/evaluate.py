import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
import yaml
import os
import mlflow
from urllib.parse import urlparse
os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/negisahil300103/machinelearningpipeline.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="negisahil300103"
os.environ["MLFLOW_TRACKING_PASSWORD"]="f6bbde60dc93d2aaae8a8836cc7d76000576bc3a"

# Load parameters from params.yaml
params = yaml.safe_load(open("params.yaml"))["train"]

def evaluate(data_path,model_path):
    data=pd.read_csv(data_path)
    X = data.drop(columns=["Outcome"])
    y = data["Outcome"]

    mlflow.set_tracking_uri("https://dagshub.com/negisahil300103/machinelearningpipeline.mlflow")

    ## load the model from the disk
    model=pickle.load(open(model_path,'rb'))

    predictions=model.predict(X)
    accuracy=accuracy_score(y,predictions)
    ## log metrics to MLFLOW

    mlflow.log_metric("accuracy",accuracy)
    print(f"Model accuracy: {accuracy}")

if __name__=="__main__":
    evaluate(params["data"],params["model"])
