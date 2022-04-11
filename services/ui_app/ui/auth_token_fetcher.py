import os
from decouple import config
import requests


def get_auth_token() -> str:
    """
    Calls tokenizator-app with secrets in URL path to get valid internal API token.
    Secrets read from local env.
    """
    credentials_login = config("CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"])
    credentials_password = config(
        "CREDENTIALS_LOGIN", os.environ["CREDENTIALS_PASSWORD"]
    )

    URL = f"http://tokenizator-app:8000/get_auth_token/{credentials_login}/{credentials_password}"
    headers = {"Content-type": "application/json"}

    response = requests.get(URL, headers=headers)
    data = response.json()
    token = data["auth_token"]

    return token
