from flask import Flask, request, jsonify
from database import Database

class Server:
    def __init__(self):
        self.server = Flask("BoardGameServer")
        self.db = Database()

        self.setup()

    def setup(self):
        @self.server.route("/boardgames", methods=["GET"])
        def boardgames():
            return self.display_games()

        @self.server.route("/add", methods=["POST"])
        def add():
            return self.add_game(request.json)
        
        @self.server.route("/check/<name>", methods=["GET"])
        def check(name):
            return self.check_game(name)
        
        @self.server.route("/delete/<name>", methods=["DELETE"])
        def delete(name):
            return self.delete_game(name)
            
            
    def display_games(self):
        return jsonify(self.db.boardGames)
    
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
        self.server.run()
    

if __name__ == "__main__":
    # Initialize and run the BoardGameServer
    board_game_server = Server()
    board_game_server.run()
