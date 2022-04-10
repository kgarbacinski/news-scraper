import jwt
from decouple import config
import os

JWT_SECRET = config('HISTORY_APP_JWT_SECRET', os.environ['HISTORY_APP_JWT_SECRET'])
JWT_ALG = config('HISTORY_APP_JWT_ALGORITHM', os.environ['HISTORY_APP_JWT_ALGORITHM'])

def token_response(token: str):
    return {
        'access_token': token
    }

def generate_JWT(): 
    token = jwt.encode(JWT_SECRET, algorithm=JWT_ALG)

    return token_response(token)

def decode_JWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        return decoded_token
    except:
        return {}