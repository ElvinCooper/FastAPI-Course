from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid
from sqlalchemy import Text


class Multimedia(SQLModel, table=True):
    __tablename__ = "multimedia"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    propiedad_id: uuid.UUID = Field(foreign_key="propiedad.id")
    url: str
    tipo: str = Field(description="imagen, video, documento_pdf, arhcivo_excel")
    es_principal: bool
    fecha_subida: datetime = Field(default_factory=datetime.now)
    descripcion: str = Field(sa_type=Text)
    cloudinary_id: int