from fastapi import FastAPI
from fastapi.responses import JSONResponse
from decouple import config
import os

from .auth_generator import generate_JWT

app = FastAPI()


@app.get("/", status_code=200)
def main_route():
    return "Running!"


@app.get("/get_auth_token/{credentials_login}/{credentials_password}", status_code=200)
def generate_token(credentials_login: str, credentials_password: str):
    if credentials_login == config(
        "CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"]
    ) and credentials_password == config(
        "CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"]
    ):
        auth_token = generate_JWT()
        return JSONResponse(auth_token)
    else:
        return "Incorrect API credentials!"
