from dataclasses import dataclass
from typing import Optional


@dataclass
class Produit:
    id: Optional = None
    name: Optional = None
    description: Optional = None
    image: Optional = None
    id_categorie: Optional = None
    date: Optional = None
    id_admin: Optional = None


@dataclass
class Categorie:
    id: Optional
    name: Optional
    id_admin: Optional

    def __str__(self):
        return "Categorie{" + str(self.id) + "," + str(self.name) + "," + str(self.id_admin) + "}"


@dataclass
class Admin:
    id: Optional = None
    email: Optional = None
    password: Optional = None

    def __str__(self):
        return "Admin{" + str(self.id) + "," + str(self.email) + "," + str(self.password) + "}"
