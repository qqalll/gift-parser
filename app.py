import os
import asyncio
from threading import Thread

# Импортируем вашего бота
from main import bot, dp

async def run_bot():
    await dp.start_polling(bot, skip_updates=True)

# Веб-сервер на Flask (это обязательно для Render)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "I'm alive!"

@app.route('/health')
def health():
    return "OK", 200

def start_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    # Запускаем веб-сервер в отдельном потоке
    web_thread = Thread(target=start_web)
    web_thread.start()
    
    # Запускаем бота
    asyncio.run(run_bot())
