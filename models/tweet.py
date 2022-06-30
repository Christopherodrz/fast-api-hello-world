# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel


class Tweet(BaseModel):
    title: str
    body: str
