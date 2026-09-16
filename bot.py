import os
import json
import urllib.request
import urllib.parse

TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text
    }).encode()
    urllib.request.urlopen(url, data=data)

offset = 0

print("Бот запущен!")

while True:
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?timeout=30&offset={offset}"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)

    for update in data["result"]:
        offset = update["update_id"] + 1

        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")

            if text == "/start":
                send_message(
                    chat_id,
                    "Привет! 👋\n\nЯ бот знакомств. ❤️\n\n"
                    "Скоро здесь можно будет создать свою анкету."
                )
