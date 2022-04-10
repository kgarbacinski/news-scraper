import jwt
from decouple import config
import os

JWT_SECRET = config('JWT_SECRET', os.environ['JWT_SECRET'])
JWT_ALG = config('JWT_ALGORITHM', os.environ['JWT_ALGORITHM'])

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