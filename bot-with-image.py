import os
import asyncio
import datetime
from flask import Flask
from threading import Thread
from telethon import TelegramClient
import logging

# Logging
logging.basicConfig(level=logging.INFO)

# Load env vars
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
recipient = os.getenv("TARGET_USERNAME")  # can be @username or group ID as string

image_path = "car.jpg"
caption_text = """欢迎来到V88汽车城租车群🫣

👍本群由【V88汽车城】官方运营，为各位老板提供专业可靠的租车服务

😊😊😊😊服务优势😊😊😊😊

👍 覆盖柬埔寨全国25个省份，支持当天送车上门
👍任何车型、任何需求，我们都能满足（轿车、SUV、商务车、皮卡、豪车等应有尽有）
👍 价格公道实惠，灵活租期，按天/周/月均可
👍 24小时在线客服，随时为您服务
👍 所有车辆定期保养，安全有保障
👍快速响应，服务专业，值得信赖

🤗 无论您在柬埔寨哪里，无论需要哪种车型，我们都可以安排！

➡️@Ai520z

➡️+855 76 668 9568

🔗 V88汽车城群 (https://t.me/Rentcar2025)🔗"""

# --- Flask keep-alive ---
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in background
Thread(target=run_web).start()

# --- Telegram Client ---
client = TelegramClient("session", api_id, api_hash)

async def send_image_loop():
    await client.start(phone)
    logging.info("✅ Telegram client logged in")

    while True:
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"[{now}] Sending image with caption...")

            if not os.path.isfile(image_path):
                logging.error("❌ Image file not found!")
                continue

            await client.send_file(
                recipient,
                file=image_path,
                caption=caption_text
            )

            logging.info(f"[{now}] ✅ Message sent")

        except Exception as e:
            logging.error(f"❌ Error: {e}")

        await asyncio.sleep(3600)  # 1 hour

# Start the bot
with client:
    client.loop.run_until_complete(send_image_loop())
