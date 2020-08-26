from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, id, username, name):
        self.id = id
        self.username = username
        self.name = name
        self.is_active = True
        self.is_authenticated = False

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)