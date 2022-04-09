import time
import jwt
from decouple import config

JWT_SECRET = config('SECRET')
JWT_ALG = config('ALGORITHM')

def token_response(token: str):
    return {
        'access_token': token
    }

def generate_JWT(): 
    payload = {
        "expires": time.time() + 999999999
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

    return token_response(token)

def decode_JWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])

        if decoded_token["expires"] >= time.time():
            return decoded_token
        else:
            return None
    except:
        return {}