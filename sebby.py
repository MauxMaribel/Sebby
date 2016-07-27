import discord
import asyncio
import re
import random
import spells

client = discord.Client()

rude_list = ['spit in your drink', 'licked the rim of the glass', 'used a dirty glass', 'dunked a roach in the drink']



@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit=100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	
	elif message.content.startswith('!spank'):
		await client.send_message(message.channel, '*Sebby turns Vexi across his knee and starts spanking her!!!*')
	elif message.content.startswith('!roll '):
		match = re.match('!roll *(\d+)d(\d+) *(choose (\d+))? *(add (\d+))', message.content)
		if match == None:
			await client.send_message(message.channel, "I don't recognize that dice roll. Try again. :)")
		else:
			ndice = int(match.group(1))
			nfaces = int(match.group(2))
			nchoose = ndice
			if match.group(4) != None:
				nchoose = int(match.group(4))

			rolls = []
			total = 0
			msg = ''
			for i in range(ndice):
				roll = random.randint(1,nfaces)
				rolls.append(roll)
				if msg != '':
					msg += ', '
				msg += str(roll)

			rolls.sort()
			rolls.reverse()
			rolls = rolls[:nchoose]
			if match.group(6) != None:
				nadd = int(match.group(6))
				total += nadd
				msg += ' + %d' % nadd
			for i in rolls:
				total += i

			await client.send_message(message.channel, "You roll %dd%d: %s = %d" % (ndice, nfaces, msg, total))
	
	elif message.content.startswith('!help'):
		msg = """
	Pathfinder Related:
		!roll
		  !roll choose
		  !roll add
		!listspells (Under Construction)
		!spellinfo spellname
		
	For Fun:
		!makeitbetter
		!makeitworse
		!makemeadrink (Under Contruction)
		!thankyou"""
		await client.send_message(message.channel, msg)
	
	elif message.content.startswith('!listspells'):
		match = re.match('!listspells (.+) (\d+)', message.content)
		temp_list = []
		pclass = match.group(1)
		level = int(match.group(2))
		temp_list.append(pclass)
		class_list = spells.find_class_spells(temp_list[0], level)
		
		if class_list == []:
			await client.send_message(message.channel, "I do not have any information for that. Try again.")
		else:
			msg = "You asked about %s level %d spells." % (temp_list[0], level)
			await client.send_message(message.channel, msg)
			def cleanspells(class_list):
				msg = ''
				for s in class_list:
					msg = msg + ('%s \n' % s)
				return msg
			result = cleanspells(class_list)
			if len(class_list) >= 60:
				result1 = class_list[0:60]
				result1 = cleanspells(result1)
				result2 = class_list[60:]
				result2 = cleanspells(result2)
				if len(class_list) >= 120:
					result2 = class_list[60:120]
					result2 = cleanspells(result2)
					result3 = class_list[120:]
					result3 = cleanspells(result3)
					await client.send_message(message.channel, result1)
					await client.send_message(message.channel, result2)
					await client.send_message(message.channel, result3)
				else:
					await client.send_message(message.channel, result1)
					await client.send_message(message.channel, result2)
			else:
				await client.send_message(message.channel, result)
		
	elif message.content.startswith('!spellinfo'):
		spell = message.content[11:]
		
		answer = spells.find_by_name(spell)
		if answer == None:
			await client.send_message(message.channel, "Sorry, that is not a valid spell. Try again.")
		else:
			msg = '%s \n' % answer['name']
			if 'classes' in answer:
				msg += 'Classes: %s \n' % answer['classes']
			if 'school' in answer:
				msg += 'School: %s \n' % answer['school']
			if 'components' in answer:
				msg += 'Components: %s \n' % answer['components']
			if 'spell_resistance' in answer:
				msg += 'Spell Resistance: %s \n' % answer['spell_resistance']
			if 'range' in answer:
				msg += 'Range: %s \n' % answer['range']
			if 'saving_throw' in answer:
				msg += 'Saving Throw: %s \n' % answer['saving_throw']
			if 'casting_time' in answer:
				msg += 'Casting Time: %s \n' % answer['casting_time']
			if 'duration' in answer:
				msg += 'Duration: %s \n' % answer['duration']
			if 'effect' in answer:
				msg += 'Effect: %s \n' % answer['effect']
			if 'url' in answer:
				msg += 'URL: %s \n' % answer['url']
			if 'description' in answer:
				msg2 = 'Description: %s \n' % answer['description']
			await client.send_message(message.channel, msg)
			await client.send_message(message.channel, msg2)
			
	elif message.content.startswith('!makeitbetter'):
		await client.send_message(message.channel, "*gives you a big hug*")
	elif message.content.startswith('!makeitworse'):
		await client.send_message(message.channel, "*mocks Vexi mercilessly*")
	elif message.content.startswith('!thankyou'):
		author = message.author
		msg = "You're very welcome {}"
		await client.send_message(message.channel,msg.format(author))
		
	elif message.content.startswith('!makemeadrink'):
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

