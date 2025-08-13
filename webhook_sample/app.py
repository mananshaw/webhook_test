from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)

    # Example of a hardcoded secret (will be flagged)
    password = "supersecretpassword123"

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000)
