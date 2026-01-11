from sqlmodel import SQLModel, Field
from validators import uuid


class RolesUsuarios(SQLModel, table=True):
    __tablename__ = "roles_usuarios"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str
