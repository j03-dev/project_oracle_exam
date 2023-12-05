import os

from flask import Blueprint, render_template, request, session, redirect
from werkzeug.utils import secure_filename

from entity import Admin, Produit
from repositories.admin_repository import AdminRepository
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository

admin_app = Blueprint('admin_app', __name__)

admin_repository = AdminRepository()
category_repository = CategoryRepository()
product_repository = ProductRepository()


def is_admin_is_authenticated() -> bool:
    try:
        if session['is_login']:
            return True
        return False
    except Exception as e:
        print(f"error{e}")
        return False


@admin_app.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        wanna_login_admin: Admin = admin_repository.get_by_email(email)
        if wanna_login_admin.password == password:
            session["is_login"] = True
            session["id_admin"] = wanna_login_admin.id
            return redirect("/?message=success login")
        return redirect("/login?message=login failed")
    return render_template("login.html")


@admin_app.route("/logout", methods=["GET"])
def logout():
    session['is_login'] = False
    return redirect("/")


app_directory = os.path.abspath(".")
upload_dir = os.path.join(app_directory, "static/image")


@admin_app.route("/add_product", methods=["get", "post"])
def add_product():
    if is_admin_is_authenticated():
        if request.method == "POST":
            name = request.form.get('name')
            description = request.form.get('description')
            image = request.files["image"]
            id_categorie = request.form.get("id_categorie")
            id_admin = int(session['id_admin'])
            image_path = os.path.join(upload_dir, secure_filename(image.filename))
            image.save(image_path)

            image = "image/" + image.filename
            produit = Produit(
                id=None, name=name, description=description, image=image, id_categorie=id_categorie, id_admin=id_admin
            )

            if product_repository.create(produit):
                return redirect("/add_product?message=add success produit")
            else:
                return redirect("/add_product?message=failed to add produit")
        else:
            categories = category_repository.get_all()
            return render_template("add_product.html", categories=categories)
    return redirect("/login")


@admin_app.route('/delete_product/<id_>', methods=["get"])
def delete_produit(id_: int):
    if is_admin_is_authenticated():
        if product_repository.delete(id_):
            return redirect(f"/?message=product {id_} is deleted ")
        else:
            return redirect(f"/?message=failed to update {id_} ")
    return redirect("/login")


@admin_app.route('/update_product/<id_>', methods=["get", "post"])
def update_product(id_: int):
    if is_admin_is_authenticated():
        if request.method == "POST":
            name = request.form.get('name')
            description = request.form.get('description')
            image = request.files.get("image")
            id_categorie = request.form.get("id_categorie")
            id_admin = int(session['id_admin'])

            if image.filename:
                image_path = os.path.join(upload_dir, secure_filename(image.filename))
                image.save(image_path)
                image = "image/" + image.filename
            else:
                image = None

            produit = Produit(
                id=id_, name=name, description=description, image=image, id_categorie=id_categorie,
                id_admin=id_admin
            )

            if product_repository.update(produit):
                return redirect(f"/update_product/{id_}?message=product {id_} is updated ")
            else:
                return redirect(f"/update_product/{id_}?message=failed to update {id_} ")
        else:
            produit = product_repository.get_by_id(id_)
            categories = category_repository.get_all()
            return render_template(
                "update_product.html", produit=produit, categories=categories,
                categorie_dao=category_repository
            )
    return redirect("/login")
