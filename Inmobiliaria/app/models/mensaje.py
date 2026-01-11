from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid
from sqlalchemy import Text, Boolean


class Mensaje(SQLModel, table=True):
    __tablename__ = "mensaje"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    emisor_id: uuid.UUID = Field(foreign_key="usuario.id")
    receptor_id: uuid.UUID = Field(foreign_key="usuario.id")
    propiedad_id: uuid.UUID = Field(foreign_key="usuario.id")
    contenido: str = Field(sa_type=Text)
    fecha_envio: datetime = Field(default_factory=datetime.now)
    leido: bool = Field(sa_type=Boolean)

