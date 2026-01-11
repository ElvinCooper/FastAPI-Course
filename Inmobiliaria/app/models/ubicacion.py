from sqlmodel import SQLModel, Field
from validators import uuid
from decimal import Decimal


class Ubicacion(SQLModel, table=True):
    __table_name__ = "ubicacion"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    pais_id: uuid.UUID = Field(foreign_key="pais.id")
    ciudad_id: uuid.UUID = Field(foreign_key="ciudad.id")
    sector: str
    calle: str
    numero: int
    codigo_postal: str
    latitud: Decimal = Field(default_factory=Decimal, max_digits=10, decimal_places=8)
    longitud: Decimal = Field(default_factory=Decimal, max_digits=11, decimal_places=8)

