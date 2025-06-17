from flask import Flask, request
import requests
import json

app = Flask(__name__)

# Настройки
BOT_TOKEN = '7744219568:AAHF2Idx8DG_fp_cD3CkvTzMj93bNlurxfw'
CHAT_ID = '-1002875185878'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print("📥 Получены данные:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        # Получаем переменные
        username = data.get("telegram_username", "-")
        vars = data.get("variables", {})

        # Формируем сообщение
        message = f"📬 Новая анкета от @{username}\n\n"
        for i in range(1, 11):
            val = vars.get(f"adform_q{i}", "-")
            message += f"{i}. Ответ: {val}\n"

        # Отправляем в Telegram
        tg_response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": message}
        )

        print("✅ Ответ Telegram:", tg_response.status_code, tg_response.text)
        return "ok"

    except Exception as e:
        print("❌ Ошибка:", e)
        return "error", 500

@app.route('/')
def home():
    return "👋 Webhook работает!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
