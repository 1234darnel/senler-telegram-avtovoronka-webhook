# main.py
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "7744219568:AAHF2Idx8DG_fp_cD3CkvTzMj93bNlurxfw"
CHAT_ID = "-1004880483658"

TEMPLATE = """#Анкета_заполнена

👤 @{username} ({first_name})

1️⃣ {q1}
2️⃣ {q2}
3️⃣ {q3}
4️⃣ {q4}
5️⃣ {q5}
6️⃣ {q6}
7️⃣ {q7}
8️⃣ {q8}
9️⃣ {q9}
🔹 {q10}
"""

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    username = data.get('telegram_username', 'неизвестен')
    first_name = data.get('first_name', 'Без имени')

    q1 = data.get('adform_q1', '-')
    q2 = data.get('adform_q2', '-')
    q3 = data.get('adform_q3', '-')
    q4 = data.get('adform_q4', '-')
    q5 = data.get('adform_q5', '-')
    q6 = data.get('adform_q6', '-')
    q7 = data.get('adform_q7', '-')
    q8 = data.get('adform_q8', '-')
    q9 = data.get('adform_q9', '-')
    q10 = data.get('adform_q10', '-')

    message = TEMPLATE.format(
        username=username,
        first_name=first_name,
        q1=q1, q2=q2, q3=q3, q4=q4, q5=q5,
        q6=q6, q7=q7, q8=q8, q9=q9, q10=q10
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )

    return {"ok": True}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
