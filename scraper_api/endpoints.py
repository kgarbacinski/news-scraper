import uvicorn
from fastapi import FastAPI

from api.scraper import ContentGetter

app = FastAPI()


@app.get("/get/{keyword}")
async def endpoint(keyword: str):

    getter = ContentGetter(keyword)
    result = getter.get()
    
    if all(not len(value) for value in result.values()):
        return {"message": f"No info with <{keyword}>"}
    else: 
        return result 


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5050)