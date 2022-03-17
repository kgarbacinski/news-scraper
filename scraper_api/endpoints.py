from fastapi import FastAPI
from fastapi.responses import JSONResponse

from computing.workers import get_response

app = FastAPI()


@app.get("/get/{keyword}")
def get_data_endpoint(keyword):
    result = get_response.delay(keyword)
    print(result)
    JSONResponse(result)
