from flask import Flask, request, jsonify, json
import mysql.connector
from BoardGame_Modify_Database_personal import Database
from BoardGame_Email import Email
# from auth import Authentication
import os           #for sending mail
import smtplib      #for sending mail
import email        #for receiving mail
import imaplib      #for receiving mail
from email.message import EmailMessage      #for sending mail

class Server:
    def __init__(self):
        self.server = Flask("BoardGameServer")
        self.db = Database()
        self.email = Email()
        # self.auth = Authentication(self.server)

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
            try:
                new_game = request.get_json()
                if not new_game:
                    return jsonify({"message": "No input data provided"}), 400
                return self.add_game(new_game)

            except Exception as e:
                return jsonify({"message": str(e)}), 500
            
        @self.server.route("/adduser", methods=["POST"])
        def adduser():
            try:
                new_user = request.get_json()
                if not new_user:
                    return jsonify({"message": "No input data provided"}), 400
                return self.add_user(new_user)

            except Exception as e:
                return jsonify({"message": str(e)}), 500
        
        @self.server.route("/check/<name>", methods=["GET"])
        def check(name):
            return self.check_game(name)
        
        @self.server.route("/checkuser", methods=["POST"])
        def checkuser():
            try:
                data = request.get_json()
                if not data:
                    return jsonify({"message": "No input data provided"}), 400
                return self.check_user(data)

            except Exception as e:
                return jsonify({"message": str(e)}), 500
        

        @self.server.route("/delete", methods=["POST"])
        def delete():
            try:
                data = request.get_json()
                if not data:
                    return jsonify({"message": "No input data provided"}), 400
                return self.delete_game(data)

            except Exception as e:
                return jsonify({"message": str(e)}), 500
        
        # Authentication routes
        @self.server.route("/login", methods=["POST"])
        def login():
            return self.auth.login(request.json)
        
        @self.server.route("/email_request", methods=["POST"])
        def email_request():
            try:
                data = request.get_json()
                if not data:
                    return jsonify({"message": "No input data provided"}), 400
                return self.email_request(data)
            
            except Exception as e:
                return jsonify({"message": str(e)}), 500
        
        # @self.server.route("/email/request", methods=["POST"])
        # def check(name):
        #     return self.check_game(name)
            
    def display_games(self):
        self.db.show_games()
        return jsonify(self.db.games_dict)
    
    def game_info(self, name):
        if name in self.db.games_dict:
            return jsonify(self.db.games_dict[name])
        else:
            return jsonify({"message": "Game not found"}), 404
    
    def add_game(self, new_game):
        self.db.addgame(new_game)
        return jsonify({"message": "Game added successfully"}), 201
    
    def add_user(self, new_user):
        self.db.adduser(new_user)
        return jsonify({"message": "User added successfully"}), 201
    
    def check_user(self, data):
        if self.db.login(data):
            return jsonify({"message": "User check successful"}), 201
        else:
            return jsonify({"message": "User check failed"}), 404
        #return jsonify({"message": "User check successful"}), 201
    
    def check_game(self, name):
        if name in self.db.boardGames:
            return jsonify({"message": "Game already exists"}), 201
        else:
            return jsonify({"message": "Game does not exist"}), 404
        
    def delete_game(self, data):
        if self.db.deletegame(data):
            return jsonify({"message": f"{data} deleted successfully"}), 201
        
    def email_request(self, data):
        self.email.send_request(data)
        return jsonify({"message": "Request sent"}), 201
    
    def run(self):
        self.server.run(debug=True)
    

if __name__ == "__main__":
    # Initialize and run the BoardGameServer
    board_game_server = Server()
    board_game_server.run()
