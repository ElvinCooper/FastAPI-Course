from typing import Callable
from fastapi import FastAPI, Request, Response
import time

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/slow")
async def slow_route():
    time.sleep(1)
    return {"Hello": "World slow"}