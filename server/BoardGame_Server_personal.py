from flask import Flask, request, jsonify, json
import mysql.connector
from BoardGame_Modify_Database_personal import Database
# from auth import Authentication

class Server:
    def __init__(self):
        self.server = Flask("BoardGameServer")
        self.db = Database()
        # self.auth = Authentication(self.server)

        self.setup()

    def setup(self):
        @self.server.route("/", methods=["GET"])
        def root():
            return jsonify({"status": "ok"})

        @self.server.route("/boardgames", methods=["GET"])
        def boardgames():
            return self.display_games()

        @self.server.route("/add", methods=["GET", "POST"])
        def add():
            return self.add_game(request.json)
        
        @self.server.route("/check/<name>", methods=["GET"])
        def check(name):
            return self.check_game(name)
        
        @self.server.route("/delete/<name>", methods=["DELETE"])
        def delete(name):
            return self.delete_game(name)
        
        # Authentication routes
        @self.server.route("/login", methods=["POST"])
        def login():
            return self.auth.login(request.json)
            
    def display_games(self):
        return jsonify(self.db.games_dict)
    
    def game_info(self, name):
        if name in self.db.games_dict:
            return jsonify(self.db.games_dict[name])
        else:
            return jsonify({"message": "Game not found"}), 404
    
    def add_game(self, new_game):
        self.db.addgame(new_game)
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
    

if __name__ == "__main__":
    # Initialize and run the BoardGameServer
    board_game_server = Server()
    board_game_server.run()
