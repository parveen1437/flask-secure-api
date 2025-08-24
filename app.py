from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/login', methods=['POST'])
def login():
    token = jwt.encode(
        {"user": "demo", "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return jsonify({"token": token})

@app.route('/secure-data', methods=['GET'])
def secure_data():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": "Secure data accessed!"})
    except:
        return jsonify({"error": "Invalid or expired token"}), 401

if __name__ == '__main__':
    app.run(debug=True)
