from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid
from decimal import Decimal
from sqlalchemy import Text


class Propiedad(SQLModel, table=True):
    __tablename__ = "propiedad"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    usuario_id: uuid.UUID = Field(foreign_key="usuario.id")
    tipo_propiedad_id: uuid.UUID = Field(foreign_key="tipo_propiedad.id")
    ubicacion_id: uuid.UUID = Field(foreign_key="ubicacion.id")
    titulo: str = Field(nullable=False)
    descripcion: str = Field(sa_type=Text)
    precio: Decimal = Field(default=0, max_digits=15, decimal_places=3)
    moneda: str = Field(nullable=False)
    tipo_operacion: str = Field(description="venta, alquiler, venta_alquiler")
    habitaciones: int
    banos: int
    area_construida: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    area_terreno: Decimal = Field(default_factory=0, max_digits=10, dicimal_places=2)
    antigueda: int
    estado: bool = Field(description="nuevo, usado, en construccion",default=True, nullable=False)
    fecha_publicacion: datetime = Field(default_factory=datetime.now)
    disponible: bool = Field(default=False, nullable=False)


class TipoPropiedad(SQLModel, table=True):
    __tablename__ = "tipo_propiedad"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str
    description: str = Field(sa_type=Text)






