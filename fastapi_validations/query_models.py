from fastapi import FastAPI, Query
from typing import Annotated, Literal
from pydantic import BaseModel, Field


app = FastAPI()

class FitlerParams(BaseModel):
    limit: Annotated[int, Field(gt=1)]
    offset: int
    order_by: Literal["created_at", "updated_at"] = "created_at"
    
    
@app.get("/items/")
async def read_items(filter_query: Annotated[FitlerParams, Query()] ):
    return {"message": "Everithing ok", **filter_query.model_dump()}