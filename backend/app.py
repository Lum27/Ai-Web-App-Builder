from flask import Flask, request, jsonify
from ai_engine import generate_site

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    client_id = data.get("client_id")
    prompt = data.get("prompt")
    site = generate_site(client_id, prompt)
    return jsonify({"site_path": site})

if __name__ == "__main__":
    app.run(debug=True)
