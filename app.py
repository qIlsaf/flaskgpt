#PROXY_API_KEY = 'sk-OnPiKHgLAp1AFxTOWgRl7FcKpFGECz4S'  ключ API
#PROXY_API_URL = 'https://api.proxyapi.ru/openai/v1/chat/completions'  URL

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']


    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer sk-OnPiKHgLAp1AFxTOWgRl7FcKpFGECz4S',
    }

    data = {
        "model": "gpt-4-turbo",
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        response = requests.post("https://api.proxyapi.ru/openai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        gpt_response = response_data['choices'][0]['message']['content']
    except Exception as e:
        gpt_response = f"Ошибка получения ответа: {e}"

    return jsonify({'response': gpt_response})


if __name__ == '__main__':
    app.run(debug=True)