from roku import Roku

from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

current_roku = None

# @app.route('/')
# def hello_world():
    # return 'Hello, World!'

@app.route('/api/choose-roku', methods=["PUT"])
def choose_roku():
    global current_roku
    req = request.get_json()
    host = req['host']

    rokus = Roku.discover()
    matches = [roku for roku in rokus if roku.host == host]
    current_roku = list(matches)[0]

    return "OK", 200

@app.route('/api/discover')
def discover():
    rokus = Roku.discover()
    hosts = list(
        map(
            lambda r: r.host,
            rokus
        )
    )

    return make_response(
        jsonify(hosts),
        200
    )

@app.route('/api/press/<button>')
def press(button):
    allowed = [
        "back",
        "down",
        "home",
        "info",
        "left",
        "right",
        "select",
        "up",
    ]
    if button in allowed:
        getattr(current_roku, button)()
        return 'OK', 200
    else:
        return 'ERROR: invalid button', 400

@app.route('/api/literal', methods=["POST"])
def literal():
    req = request.get_json()
    string = str(req['string'])

    current_roku.literal(string)

    return 'OK', 200
