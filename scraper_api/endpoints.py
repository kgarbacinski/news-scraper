import uvicorn
from fastapi import FastAPI

from api.scraper import ContentGetter

app = FastAPI()


@app.get("/get/{keyword}")
async def endpoint(keyword: str):
    getter = ContentGetter(keyword)
    result = getter.get()
    
    if all(not len(value) for value in result.values()):
        return {"message": f"No info found for: {keyword}!"}
    else: 
        return result 


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5050)

#endpoint testing with prettyprint: curl http://127.0.0.1:5050/get/ukraine | python -mjson.tool
