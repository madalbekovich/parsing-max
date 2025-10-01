from django.conf import settings
from datetime import datetime
from telegram import Bot

def send_sqlite_to_telegram():
    bot_token = None
    chat_id = None
    file_path = f'{settings.BASE_DIR}/db.sqlite3'

    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
    except FileNotFoundError:
        return None

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    caption = f"База данных на {timestamp}"

    bot = Bot(token=bot_token)

    with open(file_path, "rb") as f:
        bot.send_document(chat_id=chat_id, document=f, caption=caption)