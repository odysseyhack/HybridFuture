from flask import Flask, request, jsonify, render_template
import dashboard
from flask_basicauth import BasicAuth
import settings
from database import DATA

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = settings.BASIC_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = settings.BASIC_PASSWORD

basic_auth = BasicAuth(app)

@app.route('/', methods=['POST'])
@basic_auth.required
def index():
    r = request.json
    d = {
        "fulfillmentText": r["queryResult"]["fulfillmentText"]
    }
    DATA.MESSAGES_SINCE_START += 1
    return jsonify(d), 200

@app.route('/dashboard')
def dash():
    return dashboard.dashboard()

@app.route('/dashboard/data')
def dash_data():
    return dashboard.dashboard_data()
