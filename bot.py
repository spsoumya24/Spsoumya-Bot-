from telethon import TelegramClient, events

api_id = "15029704"   
api_hash = "ddce424a53f51a90297b29645ba6f6e3"
bot_token = "8196267301:AAH5laTLcM0RkToXRfvxsaCstMFI08rd7cY"  

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats='WhatsApp_movie'))  
async def handler(event):
    await event.forward_to('number_1_Movies_Group')  

print("Bot is running...")

client.run_until_disconnected()