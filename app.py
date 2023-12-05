from flask import Flask, render_template, request, session

from admin_app import admin_app, product_repository, category_repository, is_admin_is_authenticated

app = Flask(__name__)
app.secret_key = "24C5Bda7cB3150E20be510065B7cff9ea9caB7DA"
app.register_blueprint(admin_app)


@app.route("/")
def index():
    session["is_login"] = is_admin_is_authenticated()
    produits = product_repository.get_all()
    return render_template("index.html", produits=produits)


@app.route("/<categorie>")
def trie_par(categorie: str):
    produits = product_repository.get_all()
    c_produits = [prod for prod in produits if category_repository.get_by_id(prod.id_categorie).name == categorie]
    return render_template("index.html", produits=c_produits)


@app.route("/search", methods=["post"])
def search():
    produits = product_repository.get_all()
    if request.method == "POST":
        name = request.form.get('name')
        s_produits = [prod for prod in produits if name.lower() in prod.name.lower()]
        return render_template("index.html", produits=s_produits)


@app.route("/detail/<id_>", methods=["get"])
def detail(id_: int):
    produit = product_repository.get_by_id(id_)
    return render_template("detail.html", produit=produit)


if __name__ == "__main__":
    app.run()
