from flask import Flask, request, jsonify

server = Flask(__name__)

boardGames = {"Catan": {"playercount": "4", "gametime": "60 minutes", "age": "10", "gamecount": 5},
              "Monopoly": {"playercount": "4", "gametime": "90 minutes", "age": "8", "gamecount": 3},
              "Risk": {"playercount": "6", "gametime": "120 minutes", "age": "10", "gamecount": 2}}

# Example route: GET request with parameters
@server.route("/checkname/<name>", methods=["GET"])
def check(name):
    if name in boardGames:
        return jsonify({'message': 'Game already exists'})


@server.route("/display", methods=["GET"])
def display():
    return jsonify(boardGames)




if __name__ == "__main__":
    server.run()