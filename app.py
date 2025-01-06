from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook funcionando en Render"

@app.route("/format", methods=["POST"])
def format_comment():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    formatted_data = {
        "user": data.get("data", {}).get("from", {}).get("name", "Usuario Desconocido"),
        "message": data.get("data", {}).get("message", "Sin mensaje"),
        "post_link": data.get("data", {}).get("permalink_url", "No disponible"),
    }

    return jsonify(formatted_data), 200

if __name__ == "__main__":
    app.run(debug=True)
