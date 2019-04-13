from flask import Flask, request, jsonify, render_template
from flask_basicauth import BasicAuth
import settings

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = settings.BASIC_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = settings.BASIC_PASSWORD

basic_auth = BasicAuth(app)


class DATA:
    MESSAGES_SINCE_START = 0


@app.route('/', methods=['POST'])
@basic_auth.required
def index():
    r = request.json
    d = {
        "fulfillmentText": "hehe"
    }
    DATA.MESSAGES_SINCE_START += 1
    return jsonify(d), 200


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=DATA.MESSAGES_SINCE_START)


@app.route('/dashboard/data')
def dashboard_data():
    return jsonify(
        {
            "messages": DATA.MESSAGES_SINCE_START
        }
    )
