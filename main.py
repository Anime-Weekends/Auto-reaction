from pyrogram import Client
from config import Config as tg
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="tgbot",
            api_id=tg.API_ID,
            api_hash=tg.API_HASH,
            bot_token=tg.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.name = me.first_name
        print(f'{me.first_name} is Started...🍃')

    async def stop(self, *args):
        await super().stop()      
        print("Bot restarting.....")
       
                           
  
app = Bot()
app.run()


        










