from sqlmodel import SQLModel, Field
from validators import uuid


class Pais(SQLModel, table=True):
    __tablename__ = "pais"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str
    codigo_iso: str