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

@server.route('/add_game', methods=['POST'])
def add_game():
    data = request.get_json()  # Get JSON data from the client
    name = data.get('name')
    playercount = data.get('playercount')
    gametime = data.get('gametime')
    age = data.get('age')
    gamecount = data.get('gamecount')

    # Add the game data to the boardGames dictionary
    if name and playercount and gametime and age and gamecount:
        boardGames[name] = {
            "playercount": playercount,
            "gametime": gametime,
            "age": age,
            "gamecount": gamecount
        }
        return jsonify({'message': f'{name} has been added.', 'boardGames': boardGames}), 201
    else:
        return jsonify({'error': 'Missing data'}), 400



if __name__ == "__main__":
    server.run()