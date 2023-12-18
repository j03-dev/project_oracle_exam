from flask import Blueprint, request

from repositories.article_repository import ArticleRepository
from repositories.category_repository import CategoryRepository

article_blueprint = Blueprint("article_blueprint", __name__, url_prefix="/article")

article_repository = ArticleRepository()
category_repository = CategoryRepository()


@article_blueprint.route("", methods=["GET"])
def get_all():
    produits = article_repository.get_all()
    return produits, 200


@article_blueprint.route("/<id_>", methods=["GET"])
def retrieve(id_: int):
    produit = article_repository.get_by_id(id_)
    return produit.__dict__, 200


@article_blueprint.route("/category/<categorie>", methods=["GET"])
def article_categorie(categorie: str):
    produits = article_repository.get_by_category(categorie)
    return produits, 200


@article_blueprint.route("/search/", methods=["GET"])
def search_article():
    query = request.args.get('q', None)
    if query:
        articles = article_repository.get_all()
        articles = [
            article for article in articles if
            query.lower() in article.name.lower() or query.lower() in article.description.lower()
        ]
        return articles, 200
    else:
        return []
