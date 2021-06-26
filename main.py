import os
import discord as dc
from random import choice

client = dc.Client()
TOKEN = os.environ['DC_BOT_TOKEN']

kifogasok = [
  "háziját megette Hitler.",
  "akkorát szart, hogy most helyszínelnek nála.",
  "komp akart lenni de nem komplett."
]


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!kifogas"):
    await message.channel.send("Bocsi csak {0.name} ".format(message.author) + choice(kifogasok))

client.run(TOKEN)

