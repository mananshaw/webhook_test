from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook received:", data)

    return jsonify({"status": "received"}), 200

def is_even(n):
    return n % 2 == 1

print(is_even(2))
print(is_even(3))

if __name__ == '__main__':
    app.run(port=5000)
