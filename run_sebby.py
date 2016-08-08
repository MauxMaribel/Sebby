import discord
import asyncio
import re
import random
import spells
import sebby

client = discord.Client()

class DiscordSebby(sebby.Sebby):
	pending_messages = []
	def send_message(self, channel, msg):
		self.pending_messages.append({'message': msg, 'channel': channel})

bot = DiscordSebby()


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	
	bot.handle_message(message)
	outgoing = bot.pending_messages
	bot.pending_messages = []
	for msg in outgoing:
		await client.send_message(msg['channel'], msg['message'])
	





client.run('MjAzMDMxODU4MDU1NzQxNDQw.Cmi_pw.t1NNYKcOLz4l7LcAUdNnKTN7H0c')


