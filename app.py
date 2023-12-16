from os import getenv

import jwt
from dotenv import load_dotenv
from flask import Flask, request

from admin_app import admin_app, product_repository, category_repository
from entity import User
from repositories.user_repository import UserRepository

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.register_blueprint(admin_app)


@app.route('/login', methods=["POST"])
def login_page():
    data = request.json
    if not data:
        return {"detail": "Please provide user details"}, 400
    email = data["email"]
    password = data["password"]
    user: User = UserRepository().get_by_email(email)
    if user.password == password:
        token = jwt.encode(
            {"user_id": user.id},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return {"user": user.__dict__, "token": token}, 200
    else:
        return {"detail": "un authorized"}, 403


@app.route("/article", methods=["GET"])
def get_all():
    produits = product_repository.get_all()
    return produits, 200


@app.route("/article/<id_>", methods=["GET"])
def retrieve(id_: int):
    produit = product_repository.get_by_id(id_)
    return produit.__dict__, 200


@app.route("/article/category/<categorie>", methods=["GET"])
def article_categorie(categorie: str):
    produits = product_repository.get_all()
    produits = [prod for prod in produits if category_repository.get_by_id(prod.id_categorie).name == categorie]
    return produits, 200


@app.route("/article/search/", methods=["GET"])
def search_article():
    query = request.args.get('q', None)
    if query:
        produits = product_repository.get_all()
        produits = [
            prod for prod in produits if
            query.lower() in prod.name.lower() or query.lower() in prod.description.lower()
        ]
        return produits, 200
    else:
        return []


@app.route("/category", methods=["GET"])
def get_categories():
    categories = category_repository.get_all()
    return categories, 200


if __name__ == "__main__":
    app.run(debug=True)
