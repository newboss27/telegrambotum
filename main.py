from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Telegram ayarları
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/sinyal", methods=["POST"])
def sinyal():
    data = request.json
    mesaj = data.get("message", "⚠️ Mesaj boş geldi.")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mesaj
    }
    r = requests.post(url, json=payload)
    return {"status": "ok", "telegram_response": r.text}

@app.route("/", methods=["GET"])
def home():
    return "Bot çalışıyor! 🔥"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
