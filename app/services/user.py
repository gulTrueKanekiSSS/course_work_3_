import base64
import hashlib
import hmac

from app.dao.user import UserDao
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS



class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data, uid):
        user = self.get_one(uid)
        if data.get("username") is not None:
            user.username = data.get("username")
        if data.get("password") is not None and data.get("password2") is not None:
            if self.compare_password(data["password"]) == user.password:
                user.password = self.compare_password(data["password2"])



    def update_partial(self, data, uid):
        user = self.get_one(uid)
        if data.get('username') is not None:
            user.username = data.get('username')
        if data.get('surname') is not None:
            user.surname = data.get('surname')
        if data.get('favorite_genre') is not None:
            user.favorite_genre = data.get('favorite_genre')
        return self.dao.update(user)

    def delete(self, usid):
        return self.dao.delete(usid)

    def get_by_username(self, email):
        return self.dao.get_by_username(email)

    def get_hash(self, password):
        hash_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_password)

    def compare_password(self, password_hash, other_password):
        decoded_digist = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digist, hash_digest)
