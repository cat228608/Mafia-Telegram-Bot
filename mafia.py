import telethon
from telethon.sync import TelegramClient
from telethon import events

client = TelegramClient(
    'session',
    api_id=7769079,
    api_hash='d2858df886e25b2c588c0f9f216d05b3'
)

print("Скрипт успешно запущен!")

@client.on(events.NewMessage(from_users=468253535))
async def handle(event: events.NewMessage.Event):
    msg = event.message
    msg: telethon.types.Message
    if msg.reply_markup:
        if len(msg.reply_markup.rows) == 1 and len(msg.reply_markup.rows[0].buttons) == 1:
            gameid = msg.reply_markup.rows[0].buttons[0].url.replace('https://t.me/TrueMafiaBot?start=', '')
            await client.send_message(468253535, '/start ' + gameid)
            print("Вы зарегестрированы в игре!")
            
client.start()
client.run_until_disconnected()