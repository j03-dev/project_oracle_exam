from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/login')
def login_admin():
    return render_template("login_admin.html")


@app.route('/login')
def interface_admin():
    return render_template("admin_interface.html")


if __name__ == '__main__':
    app.run()
