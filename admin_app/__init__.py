from os.path import abspath, join as join_path

from flask import Blueprint, request
from werkzeug.utils import secure_filename

from entity import User, Article
from repositories.article_repository import ProductRepository
from repositories.category_repository import CategoryRepository
from repositories.user_repository import UserRepository
from utils import token_required

admin_app = Blueprint('admin_app', __name__)

admin_repository = UserRepository()
category_repository = CategoryRepository()
product_repository = ProductRepository()

APP_DIRECTORY = abspath(".")
UPLOAD_DIRECTORY = join_path(APP_DIRECTORY, "static/image")


@admin_app.route("/article", methods=["POST"])
@token_required
def add_product(current_user: User):
    data = request.json
    if not data:
        return {"detail": "Please provide product detail"}, 400
    name = data["name"]
    description = data["description"]
    id_categorie = data["id_category"]
    id_image = data["id_image"]

    produit = Article(
        id=None,
        name=name,
        description=description,
        id_image=id_image,
        id_categorie=id_categorie,
        id_admin=current_user.id
    )

    if product_repository.create(produit):
        return produit.__dict__, 200
    else:
        return {"detail": "failed to add produit"}, 400


@admin_app.route('/article/<id_>', methods=["PUT", "DELETE"])
@token_required
def delete_produit(current_user, id_: int):
    if request.method == "DELETE":
        if product_repository.delete(id_):
            return {"detail": f"product {id_} is deleted"}, 200
        return {"detail": f"failed to update {id_}"}, 400

    elif request.method == "PUT":
        name = request.form.get('name')
        description = request.form.get('description')
        image = request.files.get("image")
        id_categorie = request.form.get("id_categorie")

        if image.filename:
            image_path = join_path(UPLOAD_DIRECTORY, secure_filename(image.filename))
            image.save(image_path)
            image = "image/" + image.filename
        else:
            image = None

        produit = Article(
            id=id_,
            name=name,
            description=description,
            id_image=image,
            id_categorie=id_categorie,
            id_admin=current_user.id
        )

        if product_repository.update(produit):
            return produit.__dict__, 200
        return {"detail": "product not found"}, 404
