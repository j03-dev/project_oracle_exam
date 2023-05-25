import os

from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename

from doa.admin_dao import AdminDao
from doa.categorie_dao import CategorieDao
from doa.produit_dao import ProduitDao
from doa.provenance_dao import ProvenanceDao
from entity import Produit
from setting import database_connection

app = Flask(__name__)
app.secret_key = '59fd967abe98A7A1878B487C3E2c8EaC68eBfeAFCfe1d6A0Ad'
app_directory = os.path.abspath(".")
upload_dir = os.path.join(app_directory, "static/image")

# start connecting to the database
conn = database_connection()

# instance of dao (Data access object)
produit_dao = ProduitDao(conn)
provenance_dao = ProvenanceDao(conn)
categorie_dao = CategorieDao(conn)


def is_authenticate():
    if session['is_logged_in']:
        return True
    return False


@app.route('/')
def index():
    produits = produit_dao.get_all()
    return render_template("index.html", produits=produits)


@app.route('/login', methods=["GET", "POST"])
def login_admin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin_dao = AdminDao(conn)
        admin = admin_dao.get_by_email(email)

        if admin.password == password:
            session['username'] = admin.email
            session['id_admin'] = admin.id
            session['is_logged_in'] = True
            return redirect("admin")

        return render_template("login_admin.html", error="invalid credential")

    return render_template("login_admin.html")


@app.route('/admin')
def interface_admin():
    if is_authenticate():
        provenances = provenance_dao.get_all()
        categories = categorie_dao.get_all()
        return render_template("admin_interface.html", provenances=provenances, categories=categories)
    return redirect("/")


@app.route('/ajouter_categorie', methods=["POST"])
def ajouter_categorie():
    # Todo: implement add categorie
    return render_template("admin_interface.html")


@app.route('/ajouter_provenance', methods=["POST"])
def ajouter_provenance():
    # Todo: implement add provenance
    return render_template("admin_interface.html")


@app.route('/ajouter_produit', methods=["POST"])
def ajouter_produit():
    if is_authenticate():
        name = request.form.get('name')
        description = request.form.get('description')
        image = request.files["image"]
        id_provenance = request.form.get("id_provenance")
        id_categorie = request.form.get("id_categorie")
        id_admin = int(session['id_admin'])
        # upload image file
        image_path = os.path.join(upload_dir, secure_filename(image.filename))
        image.save(image_path)

        image = "image/" + image.filename

        print("id_admin", id_admin)

        produit = Produit(name=name, description=description, image=image, id_provenance=id_provenance,
                          id_categorie=id_categorie, id_admin=id_admin)

        print(produit_dao.create(produit))  # save produit-on oracle database

        return render_template("admin_interface.html")

    return redirect("login")


if __name__ == '__main__':
    app.run(debug=True)

# Todo add file input and text area for description
