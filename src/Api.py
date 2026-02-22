from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Response

import base64
from functools import wraps

from src.Calendar import Calendar

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)

cal = Calendar()

# bad practice but whatever
USERNAME = "admin"
PASSWORD = "1234"


def check_auth(auth_header):
    if not auth_header:
        return False

    try:
        auth_type, credentials = auth_header.split(" ")
        if auth_type.lower() != "basic":
            return False

        decoded = base64.b64decode(credentials).decode("utf-8")
        username, password = decoded.split(":")

        return username == USERNAME and password == PASSWORD

    except Exception:
        return False


def authenticate():
    return Response(
        "Unauthorized\n", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'}
    )


def require_basic_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not check_auth(auth_header):
            return authenticate()

        return f(*args, **kwargs)

    return decorated


# -------------------------
# GET
# -------------------------
@app.route("/calendar", methods=["GET"])
@limiter.limit("10 per minute")
@require_basic_auth
def get_calendar():
    date = request.args.get("date")

    cal = Calendar()
    if date:
        events = [e for e in cal._get_calendar() if e[0] == date]
        if not events:
            return jsonify({"error": "No events found for this date"}), 404
        return jsonify({"events": events}), 200

    return jsonify({"calendar": cal._get_calendar(), "completed": cal._get_completed()})


# -------------------------
# POST
# -------------------------
@app.route("/calendar", methods=["POST"])
@limiter.limit("5 per minute")
@require_basic_auth
def add_event():
    data = request.get_json()

    if not data or "date" not in data or "event" not in data:
        return jsonify({"error": "Missing date or event"}), 400

    cal._append_to_calendar((data["date"], data["event"]))
    return jsonify({"message": "Event added"}), 201


# -------------------------
# PUT
# -------------------------
@app.route("/calendar/complete", methods=["PUT"])
@limiter.limit("5 per minute")
@require_basic_auth
def mark_completed():
    data = request.get_json()

    if not data or "date" not in data or "event" not in data:
        return jsonify({"error": "Missing date or event"}), 400

    cal._mark_as_completed((data["date"], data["event"]))
    return jsonify({"message": "Event marked completed"})


# -------------------------
# DELETE
# -------------------------
@app.route("/calendar", methods=["DELETE"])
@require_basic_auth
def clear_all():
    cal._clear_all()
    return jsonify({"message": "Calendar cleared"})


if __name__ == "__main__":
    app.run(debug=True)
