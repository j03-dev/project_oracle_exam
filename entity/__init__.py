class Produit:
    def __init__(self, id=None, name=None, description=None, image=None, id_categorie=None, date=None,
                 id_admin=None):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.id_categorie = id_categorie
        self.data = data
        self.id_admin = id_admin


class Evolution:
    def __init__(self, id=None, date=None, prix=None, id_produit=None):
        self.id: int = id
        self.date: int = date
        self.prix: str = prix
        self.id_produit: int = id_produit


class Categorie:
    def __init__(self, id=None, name=None, id_admin=None):
        self.id = id
        self.name = name
        self.id_admin = id_admin

    def __str__(self):
        return "Categorie{" + str(self.id) + "," + str(self.name) + "," + str(self.id_admin) + "}"


class Admin:
    def __init__(self, id=None, email=None, password=None):
        self.id = id
        self.email = email
        self.password = password

    def __str__(self):
        return "Admin{" + str(self.id) + "," + str(self.email) + "," + str(self.password) + "}"
