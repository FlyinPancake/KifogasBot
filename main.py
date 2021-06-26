import os
import discord as dc
from random import choice
import json

client = dc.Client()
TOKEN = os.environ['DC_BOT_TOKEN']

kifogas_file = open("hu.json", )

kifogasok = json.load(kifogas_file)

print(kifogasok)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!kifogas"):
    await message.channel.send("Bocsi csak {0.name} ".format(message.author) + choice(kifogasok))

# client.run(TOKEN)

