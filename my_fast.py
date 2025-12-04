from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Dealer(Enum):
    Toyota = " marca toyota"
    Honda = "honda"
    Kia = "kia"


@app.get("/")
async def root():
    return "Hola FastAPI"
