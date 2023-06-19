from flask import Blueprint, render_template, request, session, redirect

from doa.admin_dao import AdminDao
from doa.categorie_dao import CategorieDao
from entity import Admin
from setting import database_connection

admin = Blueprint('admin', __name__)
connection = database_connection()
admin_dao = AdminDao(connection)
categorie_dao = CategorieDao(connection)


@admin.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        admin: Admin = admin_dao.get_by_email(email)
        if admin.password == password:
            session["is_login"] = True
            session["id_admin"] = admin.id
            return render_template("admin.html")
        return redirect("/login?message=login failed")
    return render_template("login.html")


@admin.route("/admin", methods=["get", "post"])
def admin_page():
    return render_template("admin.html")


@admin.route("/add_product", methods=["get", "post"])
def add_product():
    categories = categorie_dao.get_all()
    return render_template("add_product.html", categories=categories)
