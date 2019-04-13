from flask import Flask, request, jsonify, render_template
from database import DATA

def dashboard():
    return render_template("dashboard.html", data=DATA.MESSAGES_SINCE_START)

def dashboard_data():
    return jsonify(
        {
            "messages": DATA.MESSAGES_SINCE_START
        }
    )
