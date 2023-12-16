from entity import Image
from repositories import Repository


class ImageRepository(Repository):
    _name = "image"
    _migration_file = "image.sql"
    _object = Image
