class Produit:
    def __init__(self, id=None, name=None, description=None, image=None, id_categorie=None, id_provenance=None,
                 id_admin=None):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.id_categorie = id_categorie
        self.id_provenance = id_provenance
        self.id_admin = id_admin


class Provenance:
    def __init__(self, id=None, name=None, id_admin=None):
        self.id = id
        self.name = name
        self.id_admin = name


class Categorie:
    def __init__(self, id=None, name=None, id_admin=None):
        self.id = id
        self.name = name
        self.id_admin = id_admin


class Admin:
    def __init__(self, id=None, email=None, password=None):
        self.id = id
        self.email = email
        self.password = password

    def __str__(self):
        return "Admin{" + str(self.id) + "," + str(self.email) + "," + str(self.password) + "}"
