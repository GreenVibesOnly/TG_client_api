import os

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

app = Client('my_account', api_id, api_hash)

app.start()
app.send_message('me', 'С акка на гитхабе')
app.stop()
