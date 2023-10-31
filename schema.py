from pydantic import BaseModel
from enum import Enum


class Genre(str,Enum):
    fiction = "fiction"
    biography = "biography"
    history = "history"
    romance = "romance"
    triller = "triller"


class Book(BaseModel):
    name : str
    edition : str
    author: str
    year : int
    pages : int
    price : float
    description : str
    genre : Genre

