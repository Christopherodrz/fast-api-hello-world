# Python
import imp
from lib2to3.pgen2 import grammar
from pickletools import OpcodeInfo
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Query, Body


# from models.person import Person


app = FastAPI()


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


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
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(
        ..., ge=18, le=120, title="Alert", description="isnt in the age range!"
    ),
):
    return {name: age}
