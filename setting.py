from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
DB_NAME = getenv("DB_NAME")
