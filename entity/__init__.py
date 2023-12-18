from dataclasses import dataclass
from typing import Optional


@dataclass
class Article:
    id: Optional = None
    name: Optional = None
    description: Optional = None
    image_id: Optional = None
    category_id: Optional = None
    date: Optional = None
    user_id: Optional = None


@dataclass
class Categorie:
    id: Optional = None
    name: Optional = None
    user_id: Optional = None


@dataclass
class User:
    id: Optional = None
    username: Optional = None
    first_name: Optional = None
    last_name: Optional = None
    email: Optional = None
    password: Optional = None


@dataclass
class Image:
    id: int = None
    path: str = None
