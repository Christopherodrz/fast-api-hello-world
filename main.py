# Python
import imp
from lib2to3.pgen2 import grammar
from pickletools import OpcodeInfo
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Path, Query, Body


# from models.person import Person


app = FastAPI()

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


class Location(BaseModel):
    city: str
    state: str
    country: str


@app.get("/")
def home():
    return {"Hello": "World"}


# Request and response body


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# Validations: Query Parameters


@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Name",
        description="It's between 1 and 50 characters!",
    ),
    age: int = Query(
        ...,
        ge=18,
        le=120,
        title="Age",
        description="isnt in the age range!",
    ),
):
    return {name: age}


# Validations: Path Parameters


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Id",
        description="Can not be less than 1!",
    )
):
    return {person_id: "It exists!"}


# Validations: Request Body


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Id",
        description="This is the person Id",
        gt=0,
    ),
    person: Person = Body(...),
    location: Location = Body(...),
):
    result = person.dict()
    result.update(location.dict())

    return result
