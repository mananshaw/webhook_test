# Webhook Sample (Flask)

A simple Python Flask application that receives webhooks.

## 🚀 How to Run

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the app:

    ```bash
    python app.py
    ```

3. Use ngrok to expose it publicly:

    ```bash
    ngrok http 5000
    ```

4. Add the generated URL (e.g. https://abc123.ngrok.io/webhook) as a webhook endpoint in GitHub or any service.

## 📬 Webhook Endpoint

- URL: `/webhook`
- Method: `POST`
- Content-Type: `application/json`
