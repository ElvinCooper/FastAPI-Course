from sqlmodel import SQLModel, Field
from validators import uuid
from datetime import datetime


class Favorito(SQLModel, table=True):
    __tablename__ = "favorito"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    usuario_id: uuid.UUID = Field(foreign_key="usuario.id")
    propiedad_id: uuid.UUID = Field(nullable=False)



