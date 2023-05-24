from flask import Flask, render_template, request, redirect, url_for, session

from doa.admin_dao import AdminDao
from setting import database_connection

app = Flask(__name__)
app.secret_key = '59fd967abe98A7A1878B487C3E2c8EaC68eBfeAFCfe1d6A0Ad'

conn = database_connection()


def is_authenticate():
    if session['is_logged_in']:
        return True
    return False


@app.route('/')
def index():
    # Todo get all produit from database
    return render_template("index.html")


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
            print("is authenticated")
            return redirect("admin")

        return render_template("login_admin.html", error="invalid credential")

    return render_template("login_admin.html")


@app.route('/admin')
def interface_admin():
    if is_authenticate():
        return render_template("admin_interface.html")
    return redirect("/")


@app.route('/ajouter_categorie', methods=["POST"])
def ajouter_categorie():
    # Todo: implement add categorie
    return render_template("admin_interface.html")


@app.route('/ajouter_provenance', methods=["POST"])
def ajouter_provenance():
    # Todo: implement add provenance
    return render_template("admin_interface.html")


if __name__ == '__main__':
    app.run(debug=True)
