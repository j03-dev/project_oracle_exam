from flask import Blueprint

from repositories.category_repository import CategoryRepository

category_blueprint = Blueprint("category_blueprint", __name__)

category_repository = CategoryRepository()


@category_blueprint.route("/category", methods=["GET"])
def get_categories():
    categories = category_repository.all()
    return categories, 200
