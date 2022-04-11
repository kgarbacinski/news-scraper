import jwt
from decouple import config
import os
import time

JWT_SECRET = config("JWT_SECRET", os.environ["JWT_SECRET"])
JWT_ALG = config("JWT_ALGORITHM", os.environ["JWT_ALGORITHM"])


def token_response(token: str):
    return {"auth_token": token}


def generate_JWT():
    payload = {"expires": time.time() + 5555}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

    return token_response(token)
