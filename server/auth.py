from flask import jsonify

class Authentication:
    def login(self, data):
        if data["username"] == "admin" and data["password"] == "admin":
            return True
        else:
            return False

