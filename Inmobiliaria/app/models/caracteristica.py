from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid


class Caracteristica(SQLModel, table=True):
    __tablename__ = "caracteristica"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str
    categoria: str


class PropiedadCaracteristica(SQLModel, table=True):
    __tablename__ = "propiedad_caracteristica"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
