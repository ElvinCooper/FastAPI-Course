# OAuth 2
# OAuth 1
# OpenID Connect
# OpenID

from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from rich import status

app = FastAPI()


oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return token


# ------- Exception personalizada ---------- #
my_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
