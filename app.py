from fastapi import FastAPI
from api import logistic_regression

app = FastAPI()

app.include_router(logistic_regression.router)

@app.get('/')
async def hello_world():
    return {"message": "Hello, World!"}
