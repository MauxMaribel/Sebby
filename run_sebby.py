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
	
	##everything below here needs to be moved into sebby.py with the new way of doing things.	
		
	if message.content.startswith('!makemeadrink'):
		await client.send_message(message.channel, "What can I get you to drink?")	
	
		drink = await client.wait_for_message(timeout=14, author=message.author)
		match = re.match('(.+) (please)?', message.content)	

		if match == None:
			await client.send_message(message.channel, "Don't waste my time mortal.")
		elif match.group(2) != None:
			drink = match.group(1)
			msg = "Enjoy your {}"
			await client.send_message(message.channel, msg.format(drink))
		else:	
			drink = match.group(1)
			await client.send_message(message.channel, drink)
			msg = "Sebby steps away and shortly comes back with a delicious {}."
			await client.send_message(message.channel, msg.format(drink))
			await client.send_message(message.channel, "*Sebby comes back after a couple minutes.* Did you enjoy your drink?")
		
			answer = await client.wait_for_message(timeout=10, author= message.author)
			if answer == 'yes' or 'Yes':
				msg = "*Sebby grins, then nods. He steps away with the satisfaction of knowing he %s.* " % random.choice(rude_list)
				await client.send_message(message.channel, msg)
			else:
				await client.send_message(message.channel, "*Sebby nods, walking away looking quite agitated.*")




client.run('MjAzMDMxODU4MDU1NzQxNDQw.Cmi_pw.t1NNYKcOLz4l7LcAUdNnKTN7H0c')


