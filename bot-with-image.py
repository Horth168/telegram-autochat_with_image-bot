from flask import Flask
from threading import Thread
from telethon.sync import TelegramClient
import time, os

# Env variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
recipient = os.getenv("TARGET_USERNAME")

client = TelegramClient('session', api_id, api_hash)

# Flask app for UptimeRobot
app = Flask(__name__)
@app.route('/')
def home():
    return "✅ Bot is alive and running"

# Flask thread
def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Main image-sending loop
def send_loop():
    with client:
        while True:
            client.send_file(
                recipient,
                'car.jpg',
                caption="""欢迎来到V88汽车城租车群🫣

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
            )
            print("✅ Image sent! Sleeping for 1 hour.")
            time.sleep(3600)

# Start both processes
Thread(target=run_flask).start()
Thread(target=send_loop).start()

