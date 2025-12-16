from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()


# ---------------------- Inyeccion de dependencias ejemplo No.1 -------------------- #

class AuthService:
    @staticmethod
    def authenticate(token: str):
        if token == "valid-token":
            return True
        else:
            raise HTTPException(status_code=401, detail="Invalid token")


def get_auth_service():
    return AuthService()


auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]


@app.get("/secure-data/")
def get_secure_data(token: str, auth_service: auth_service_dependency):
    if auth_service.authenticate(token):
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid token")


# ---------------------- Inyeccion de dependencias ejemplo No.2 -------------------- #
def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit, "q": q}


@app.get("/items/")
def get_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons