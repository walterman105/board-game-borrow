from time import sleep
from flask import Flask, request, jsonify
from database import Database
from auth import Authentication

class Server:
    def __init__(self):
        self.server = Flask("BoardGameServer")
        self.db = Database()
        self.auth = Authentication()

        self.setup()

    def setup(self):
        @self.server.route("/", methods=["GET"])
        def root():
            return jsonify({"status": "ok"})

        @self.server.route("/boardgames", methods=["GET"])
        def boardgames():
            return self.display_games()
        
        @self.server.route("/add", methods=["POST"])
        def add():
            return self.add_game(request.json)
        
        @self.server.route("/info/<name>", methods=["GET"])
        def info(name):
            return self.game_info(name)

        @self.server.route("/check/<name>", methods=["GET"])
        def check(name):
            return self.check_game(name)
        
        @self.server.route("/delete/<name>", methods=["DELETE"])
        def delete(name):
            return self.delete_game(name)
        
        # Authentication routes
        @self.server.route("/login", methods=["POST"])
        def login():
            return self.user_login(request.json)
            
    def display_games(self):
        #return jsonify(self.db.boardGames)
        return jsonify(self.db.get_game_names())
    
    def game_info(self, name):
        if name in self.db.boardGames:
            return jsonify(self.db.boardGames[name])
        else:
            return jsonify({"message": "Game not found"}), 404

    def add_game(self, data):
        self.db.add_game(data)
        return jsonify({"message": "Game added successfully"}), 201
    
    def check_game(self, name):
        if name in self.db.boardGames:
            return jsonify({"message": "Game already exists"}), 200
        else:
            return jsonify({"message": "Game does not exist"}), 404
        
    def delete_game(self, name):
        if self.db.delete_game(name):
            return jsonify({"message": f"{name} deleted successfully"}), 200
        else:
            return jsonify({"message": f"{name} not found"}), 404
    
    def run(self):
        self.server.run(debug=True)

    def user_login(self, data):
        success = self.auth.login(data)
        if success:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Login failed"}), 401
    

if __name__ == "__main__":
    # Initialize and run the BoardGameServer
    board_game_server = Server()
    board_game_server.run()
