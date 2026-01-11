from sqlmodel import SQLModel, Field
from datetime import datetime
from validators import uuid
from sqlalchemy import Text


class Cita(SQLModel, table=True):
    __tablename__ = "cita"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    usuario_id: uuid.UUID = Field(default = uuid.uuid4, primary_key=True)
    fecha_hora: datetime = Field(default_factory=datetime.now)
    estado: bool = Field(default_factory=bool)
    notas: str = Field(sa_type=Text)
    fecha_registro: datetime = Field(default_factory=datetime.now)
