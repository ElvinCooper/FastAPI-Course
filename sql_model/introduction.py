from sqlmodel import create_engine, Field, SQLModel, Session, select
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from contextlib import asynccontextmanager


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


# modelo publico para respuestas de la API
class HeroPublic(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    secret_name: str


class HeroUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    sqlite_url,
    connect_args={
        "check_same_thread": False
})


def create_dn_and_table():
    SQLModel.metadata.create_all(engine)


# crear session y dependencia
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# Lifespan Events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # aqui iria el codigo para ejecutar antes
    create_dn_and_table()
    yield
    # aqui el codigo para ser ejecutado despues de terminado el programa.


app = FastAPI(lifespan=lifespan)


