from sqlmodel import create_engine, Field, SQLModel, Session, select, Relationship
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query, status
from contextlib import asynccontextmanager


# modelo base
class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="team")


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

class TeamPublic(TeamBase):
    id: int


# modelo public para respuestas de la API
class HeroPublic(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team_id: int | None = None


class HeroCreate(HeroBase):
    team_id: int | None = None
    secret_name: str


class HeroUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None
    team_id: int | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    sqlite_url,
    connect_args={
        "check_same_thread": False
})


def create_dn_and_table():
    SQLModel.metadata.create_all(engine)


# crear session y dependencia
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# Lifespan Events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # aqui iria el codigo para ejecutar antes
    create_dn_and_table()
    yield
    # aqui el codigo para ser ejecutado despues de terminado el programa.


app = FastAPI(lifespan=lifespan)


# Get heroes
@app.get("/heroes/", response_model=list[HeroPublic])
async def get_heroes(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


# Get Hero by ID
@app.get("/heroes/{heroe_id}", response_model=HeroPublic)
def get_hero(heroe_id: int, session: SessionDep):
    hero = session.get(Hero, heroe_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Not found")
    return hero


# Crear un nuevo Heroe
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


# update a Heroe
@app.patch("/heroe/{hero_id}", response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.commit()
    session.refresh(hero_db)
    return hero_db


# delete a Hero
@app.delete("/heroe/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(hero_db)
    session.commit()

    return status.HTTP_204_NO_CONTENT


# ------ Endpoint para Teams -------------#
@app.post("/teams/", response_model=TeamPublic)
def crear_team(team: TeamCreate, session: SessionDep):
    db_team = Team.model_validate(team)
    session.add(db_team)
    session.commit()
    session.refresh(db_team)
    return db_team


# get team by its id
@app.get("/teams/{team_id}", response_model=TeamPublic)
def get_team(team_id: int, session: SessionDep):
    team = session.get(Team, team_id)
    if not team_id:
        raise HTTPException(status_code=404, detail="Not found")
    return team


# delete team by id
@app.delete("/teams/{team_id}", response_model=TeamPublic)
def delete_team(team_id: int, session: SessionDep):
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Not found")
    # Opcion 1 team_id = None en todos los heroes
    for hero in team.heroes:
        hero.team_id = None
        hero.team = None
    session.delete(team)
    session.commit()
    return status.HTTP_204_NO_CONTENT


# option 2 Borrar todos los heroes del equipo
#  for heroe in heroes:
#     session.delete(heroe)
#  session.commit()
#  return status.HTTP_204_NO_CONTENT

