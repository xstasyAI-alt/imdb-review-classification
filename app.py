from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import logistic_regression

app = FastAPI()

app.include_router(logistic_regression.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}
