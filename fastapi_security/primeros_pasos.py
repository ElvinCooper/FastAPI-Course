# OAuth 2
# OAuth 1
# OpenID Connect
# OpenID

from fastapi import Depends, FastAPI
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return token