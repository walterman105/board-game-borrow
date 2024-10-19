from flask import jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

class Authentication:
    def __init__(self, app):
        self.app = app
        self.bcrypt = Bcrypt(self.app)

        self.app.config["JWT_SECRET_KEY"] = "949dc3a8-gabe-matt-lex-9fe1096ad3b9"
        self.jwt = JWTManager(self.app)

        self.users_db_test = {
            "user1": self.bcrypt.generate_password_hash("password123").decode("utf-8"),
        }

        def register(self, data):
            username = data.get("username")
            password = data.get("password")
            
            if not username or not password:
                return jsonify({"error": "Missing username or password"}), 400
            
            if username in self.users_db_test:
                return jsonify({"error": "Username already exists"}), 400
            
            hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')
            self.users_db_test[username] = {"password": hashed_password}

            return jsonify({"message": "User registered successfully"}), 201

        def login(self, data):
            username = data.get("username")
            password = data.get("password")
            
            if not username or not password:
                return jsonify({"error": "Missing username or password"}), 400
            
            user = self.users_db_test.get(username)
            if not user or not self.bcrypt.check_password_hash(user['password'], password):
                return jsonify({"error": "Invalid username or password"}), 401
            
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        

        # Example route that requires JWT authentication
        @app.route('/protected', methods=['GET'])
        @jwt_required()
        def protected():
            current_user = get_jwt_identity()
            return jsonify(logged_in_as=current_user)


        # Example of a route protected by JWT to add a board game
        @app.route('/add_game', methods=['POST'])
        @jwt_required()
        def add_game():
            current_user = get_jwt_identity()  # Get the current authenticated user
            data = request.json
            # Your existing game adding logic here
            return jsonify({"message": f"Game added by {current_user}"}), 201

