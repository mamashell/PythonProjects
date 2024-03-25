import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme/wholesomememes')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

#this is a special addition that displays a gif I created in another Python project
    if message.content.startswith('$touch'): 
      with open("the_touch.gif", "rb") as file:
        touch_gif = discord.File(file)
      await message.channel.send(file = touch_gif)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTIyMTMzMzA4Mzk1ODE0OTE2MA.Gs9pUq.FUByGjUSEgCWv1D7YuvOT5FODQDTPTT3VIlA8o') # Replace with your own token.
