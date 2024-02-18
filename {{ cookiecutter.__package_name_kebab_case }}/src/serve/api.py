"""{{ cookiecutter.package_name }} REST API."""
import json
import os

import boto3
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from mangum import Mangum
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

ENDPOINT = os.environ.get("DEPLOY_SHA")
sagemaker_runtime = boto3.client("sagemaker-runtime")

app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)

@app.get("/")
def read_root() -> str:
    """Read root."""
    return "You have reached the Sagemaker Endpoint. Please make a POST request to /predict with a file."

@app.post("/predict")
async def predict_file(file: UploadFile = File(...)) -> dict:
    """Predict file."""
    contents = await file.read()
    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType="application/octet-stream",  # Change this depending on your payload format
            Accept="application/json",
            Body=contents,
        )
    except Exception as e:
        raise (e)
    prediction = json.loads(response["Body"].read().decode("utf-8"))
    return {
        "filename": file.filename,
        "prediction": prediction["prediction"][0],
    }


handler = Mangum(app)