from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid
from sqlalchemy import Text


class Documento(SQLModel, table=True):
    __tablename__ = "documento"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    tipo_documento_id: uuid.UUID = Field(foreign_key="tipo_documento.id")
    propiedad_id: uuid.UUID = Field(foreign_key="propiedad.id")
    nombre: str
    url: str
    cloudinary_id: int
    description: str = Field(sa_type=Text)
    fecha_subido: datetime = Field(default_factory=datetime.now)


class TipoDocumento(SQLModel, table=True):
    __tablename__ = "tipo_documento"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str


