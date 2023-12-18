from os import getenv

from dotenv import load_dotenv
from flask import Flask

from blueprints import category_blueprint, article_blueprint, user_blueprint

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.register_blueprint(article_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
