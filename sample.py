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

@app.route('/api/info')
def info():
    current_roku.info()

    return 'OK', 200

@app.route('/api/up')
def up():
    current_roku.up()
    return 'OK', 200

@app.route('/api/down')
def down():
    current_roku.down()
    return 'OK', 200

@app.route('/api/left')
def left():
    current_roku.left()
    return 'OK', 200

@app.route('/api/right')
def right():
    current_roku.right()
    return 'OK', 200

@app.route('/api/select')
def select():
    current_roku.select()

    return 'OK', 200

@app.route('/api/literal', methods=["POST"])
def literal():
    req = request.get_json()
    string = str(req['string'])

    current_roku.literal(string)

    return 'OK', 200
