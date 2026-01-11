from datetime import datetime
from sqlmodel import create_engine, Field, SQLModel, Session, select, Relationship
from fastapi import Depends, FastAPI, HTTPException, Query, status
from validators import uuid
from pydantic import EmailStr


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    nombre: str
    email: str = EmailStr()
    password: str = Field(nullable=False)
    telefono: str | None = None
    tipo_usuario: str = Field(nullable=False, description="cliente, agente, administrador")
    fecha_registro: datetime = Field(default_factory=datetime.now)
    activo: bool = Field(default=True)