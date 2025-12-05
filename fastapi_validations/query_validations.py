from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items')
async def read_items(q: Annotated[list[str] | None, Query()] = None):
	results: dict = {"message": "Acesso a get(read_items)"}
	if q:
		results.update({"q": q})
     return results		
