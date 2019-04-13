from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import settings

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = settings.BASIC_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = settings.BASIC_PASSWORD

basic_auth = BasicAuth(app)


@app.route('/', methods=['POST'])
@basic_auth.required
def secret_view():
    r = request.json
    d = {
        "fulfillmentText": "hehhe"
    }
    return "", 200
