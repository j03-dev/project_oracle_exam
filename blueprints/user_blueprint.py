from dataclasses import dataclass

import jwt
from flask import Blueprint, request

from entity import User
from repositories.user_repository import UserRepository
from setting import SECRET_KEY
from utils import token_required, deserialize

user_repository = UserRepository()
user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/user")


@dataclass
class Credential:
    email: str
    password: str


@user_blueprint.route("/login", methods=["POST"])
def login():
    credential = deserialize(request.json, Credential)
    user = user_repository.get(email=credential.email)
    if user and user.password == credential.password:
        token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")
        return {"user": user.__dict__, "token": token}, 200
    else:
        return {"detail": "un authorized"}, 403


@user_blueprint.route("", methods=["POST"])
def register():
    user: User = deserialize(request.json, User)
    message, code = "success", 201
    if not user_repository.create(user):
        message, code = "failed", 404
    return {"detail": f"add user is {message}"}, code


@user_blueprint.route("", methods=["PUT", "DELETE", "GET"])
@token_required
def manage(current_user: User):
    if request.method == "GET":
        return current_user.__dict__, 200
    elif request.method == "PUT":
        user: User = deserialize(request.json, User)
        user.id = current_user.id
        message, code = "success", 200
        if not user_repository.update(user):
            message, code = "failed", 404
        return {"detail": f"update user is {message}"}, code
    elif request.method == "DELETE":
        message, code = "success", 202
        if not user_repository.delete(current_user.id):
            message, code = "failed", 404
        return {"detail": f"delete user is {message}"}, code