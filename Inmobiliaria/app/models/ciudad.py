from sqlmodel import SQLModel, Field
from validators import uuid

class Cuidad(SQLModel, table=True):
    __tablename__ = "cuidad"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    pais_id: uuid.UUID = Field(foreign_key="pais.id")
    nombre: str
    codigo_postal: str
    activo: bool
