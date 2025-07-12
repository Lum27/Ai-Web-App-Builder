from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import generate_site
from stripe_webhook import stripe_webhook

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication
app.register_blueprint(stripe_webhook, url_prefix="/stripe")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    client_id = data.get("client_id")
    prompt = data.get("prompt")
    site_path = generate_site(client_id, prompt)
    return jsonify({
        "site_path": site_path,
        "url": f"/client-sites/{client_id}/index.html"
    })

if __name__ == "__main__":
    app.run(debug=True)
