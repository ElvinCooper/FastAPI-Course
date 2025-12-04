from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional


class Usuario(BaseModel): 
    id : int
    nombre: str
    email: str
    edad: int | None = None
    activo : bool
    
app = FastAPI()    

@app.get("/users/")
def users():
    ...
    
    
@app.post("/users/")    
def user_create(user: Usuario):
    return {
        "message": f"User {user.email} creado exitosamente",
        "datos": user
    }
    
@app.put("/users/{user_id}")    
def user_update(user_id: int, user: Usuario, query: str | None = None):
    result : dict = {"user_id": user_id, **user.model_dump()}
    if query:
        result.update({"query": query})
    return result