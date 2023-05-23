class Produit:
    def __init__(self, id=None, name=None, image=None, id_categorie=None, id_provenance=None):
        self.id = id
        self.name = name
        self.image = image
        self.id_categorie = id_categorie
        self.id_provenance = id_provenance


class Provenance:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


class Categorie:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
