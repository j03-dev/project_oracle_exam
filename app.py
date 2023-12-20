from flask import Flask

from blueprints import category_blueprint, article_blueprint, user_blueprint
from setting import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(article_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
