from flask import Flask, render_template, request

from admin.app import admin
from admin.app import categorie_dao, produit_dao

app = Flask(__name__)
app.secret_key = "24C5Bda7cB3150E20be510065B7cff9ea9caB7DA"
app.register_blueprint(admin)

produits = produit_dao.get_all()


@app.route("/")
def index():
    return render_template("index.html", produits=produits)


@app.route("/<categorie>")
def trie_par(categorie):
    global produits
    c_produits = [prod for prod in produits if categorie_dao.get_by_id(prod.id_categorie).name == categorie]
    return render_template("index.html", produits=c_produits)


@app.route("/search", methods=["post"])
def search():
    global produits
    if request.method == "POST":
        name = request.form.get('name')
        print(name)
        s_produits = [prod for prod in produits if name.lower() in prod.name.lower()]
        return render_template("index.html", produits=s_produits)


if __name__ == "__main__":
    app.run(debug=True)
