from flask import Flask, render_template

from admin.app import admin
from doa.categorie_dao import CategorieDao
from doa.produit_dao import ProduitDao
from setting import database_connection

app = Flask(__name__)
app.secret_key = "24C5Bda7cB3150E20be510065B7cff9ea9caB7DA"
app.register_blueprint(admin)

connection = database_connection()
produit_dao = ProduitDao(connection)
categorie_dao = CategorieDao(connection)


@app.route("/")
def index():
    produits = produit_dao.get_all()
    return render_template("index.html", produits=produits, categorie_dao=categorie_dao)


if __name__ == "__main__":
    app.run(debug=True)
