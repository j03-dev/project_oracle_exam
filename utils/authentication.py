from functools import wraps

import jwt
from flask import request

from repositories.user_repository import UserRepository
from setting import SECRET_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            headers = request.headers.get("Authorization", "").split()
            if headers and len(headers) == 2:
                _, token = headers
        if not token:
            return {"detail": "Authentication Token is missing!"}, 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = UserRepository().get(id=data["user_id"])
            if current_user is None:
                return {"detail": "Invalid Authentication token!"}, 401
            return f(current_user, *args, **kwargs)
        except Exception as e:
            return {"detail": str(e)}, 500

    return decorated
