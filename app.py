import os

from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename

from doa.admin_dao import AdminDao
from doa.categorie_dao import CategorieDao
from doa.produit_dao import ProduitDao
from doa.provenance_dao import ProvenanceDao
from entity import Produit, Categorie, Provenance
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


def is_admin_is_authenticated() -> bool:
    try:
        if session['is_logged_in']: return True
        return False
    except Exception as e:
        print(f"error{e}")
        return False


@app.route('/')
def index():
    produits = produit_dao.get_all()
    return render_template("index.html", produits=produits, provenance_dao=provenance_dao, categorie_dao=categorie_dao,
                           is_authenticated=is_admin_is_authenticated)


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

        return render_template("admin_login.html", error="invalid credential",
                               is_authenticated=is_admin_is_authenticated)

    return render_template("admin_login.html", is_authenticated=is_admin_is_authenticated)


@app.route("/logout", methods=["GET"])
def logout():
    session['is_logged_in'] = False
    return redirect("/")


@app.route("/admin", methods=["GET"])
def interface_admin():
    if is_admin_is_authenticated():
        produits = produit_dao.get_all()
        return render_template("index.html", produits=produits, provenance_dao=provenance_dao,
                               categorie_dao=categorie_dao, is_authenticated=is_admin_is_authenticated)
    return redirect("login")


@app.route('/ajouter_categorie', methods=["POST", "GET"])
def create_categorie():
    if is_admin_is_authenticated():
        if request.method == "POST":
            name = request.form.get("name")
            id_admin = session["id_admin"]
            if categorie_dao.create(Categorie(name=name, id_admin=id_admin)):
                response = "categorie a été ajouter avec succès"
                return render_template("ajouter_categorie.html", is_authenticated=is_admin_is_authenticated,
                                       succes=response)
            response = "votre opération ne ses pas terminer correctement"
            return render_template("ajouter_categorie.html", is_authenticated=is_admin_is_authenticated, error=response)

        return render_template("ajouter_categorie.html", is_authenticated=is_admin_is_authenticated)
    return redirect("login")


@app.route('/maj_categorie/<int:id_>', methods=["POST", "GET"])
def update_categorie(id_: int):
    if is_admin_is_authenticated():
        categorie = categorie_dao.get_by_id(id_)
        if request.method == "POST":
            name = request.form.get("name")
            id_admin = session["id_admin"]
            categorie_dao.update(Categorie(id_, name, id_admin))
            return redirect("/")

        return render_template("maj_categorie.html", categorie=categorie, is_authenticated=is_admin_is_authenticated)

    return redirect("login")


@app.route('/effacer_categorie/<int:id_>', methods=["POST"])
def delete_categorie(id_: int):
    if is_admin_is_authenticated():
        if categorie_dao.delete(id_):
            return redirect("/")
    return redirect("/login")


@app.route('/ajouter_provenance', methods=["POST", "GET"])
def ajouter_provenance():
    if is_admin_is_authenticated():
        if request.method == "POST":
            name = request.form.get("name")
            id_admin = session["id_admin"]
            if provenance_dao.create(Provenance(name=name, id_admin=id_admin)):
                response = "provenance a été ajouter avec succès"
                return render_template("ajouter_provenance.html", is_authenticated=is_admin_is_authenticated,
                                       succes=response)
            response = "votre opération ne ses pas terminer correctement"
            return render_template("ajouter_provenance.html", is_authenticated=is_admin_is_authenticated,
                                   error=response)

        return render_template("ajouter_provenance.html", is_authenticated=is_admin_is_authenticated)

    redirect("/login")


@app.route('/effacer_provenance/<int:id_>', methods=["POST"])
def delete_provenance(id_: int):
    if is_admin_is_authenticated():
        if provenance_dao.delete(id_):
            return redirect("/")
    return redirect("/login")


@app.route('/maj_provenance/<int:id_>', methods=["POST", "GET"])
def update_provenance(id_: int):
    if is_admin_is_authenticated():
        provenance = provenance_dao.get_by_id(id_)
        if request.method == "POST":
            name = request.form.get("name")
            id_admin = session["id_admin"]
            provenance_dao.update(Provenance(id=id_, name=name, id_admin=id_admin))
            return redirect("/")

        return render_template("maj_provenance.html", provenance=provenance, is_authenticated=is_admin_is_authenticated)

    return redirect("/login")


@app.route('/ajouter_produit', methods=["POST", "GET"])
def ajouter_produit():
    if is_admin_is_authenticated():
        if request.method == "POST":
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

            produit = Produit(name=name, description=description, image=image, id_provenance=id_provenance,
                              id_categorie=id_categorie, id_admin=id_admin)

            produit_dao.create(produit)  # save produit-on oracle database

            return render_template("ajouter_produit.html", is_authenticated=is_admin_is_authenticated)
        else:
            provenances = provenance_dao.get_all()
            categories = categorie_dao.get_all()
            return render_template("ajouter_produit.html", provenances=provenances, categories=categories,
                                   is_authenticated=is_admin_is_authenticated)

    return redirect("login")


@app.route('/effacer_produit/<id_>', methods=["POST"])
def delete_produit(id_: int):
    if is_admin_is_authenticated():
        if produit_dao.delete(id_):
            response = "produit a été effacer avec succès"
            return redirect("/")
        return redirect("/")
    return redirect("login")


@app.route('/maj_produit/<id_>', methods=["POST", "GET"])
def update_produit(id_: int):
    if is_admin_is_authenticated():
        produit = produit_dao.get_by_id(id_)
        if request.method == "POST":
            name = request.form.get('name')
            description = request.form.get('description')
            image = request.files["image"]
            id_provenance = request.form.get("id_provenance")
            id_categorie = request.form.get("id_categorie")
            id_admin = int(session['id_admin'])

            image_path = os.path.join(upload_dir, secure_filename(image.filename))
            image.save(image_path)

            image = "image/" + image.filename
            produit = Produit(id=id_, name=name, description=description, image=image, id_provenance=id_provenance,
                              id_categorie=id_categorie, id_admin=id_admin)

            if produit_dao.update(produit):
                return redirect("/")
        else:
            return render_template("maj_produit.html", produit=produit, categorie_dao=categorie_dao,
                                   provenance_dao=provenance_dao, is_authenticated=is_admin_is_authenticated)

    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True)
