import re

def LetterString(text):
	return re.match('[a-zA-Z]+$', text) != None

def IsWholeNumber(text):
	return re.match('\d+$', text) != None
	
def ReturnNumber(text):
	match = re.search('[0-9]+', text)
	if match != None:
		print (match.group(0))
	else:
		print ('There is no number in this string')
		
print (ReturnNumber('4Fuck you'))

		
print (IsWholeNumber('42'))
print (IsWholeNumber('4345'))
print (IsWholeNumber('4824249'))
print (IsWholeNumber('-42922'))
print (LetterString('0'))
print (ReturnNumber('4Fuck you'))
print (LetterString('hello'))
print (LetterString(''))


	##everything below here needs to be moved into sebby.py with the new way of doing things.	
		
#	if message.content.startswith('!makemeadrink'):
#		await client.send_message(message.channel, "What can I get you to drink?")	
#	
#		drink = await client.wait_for_message(timeout=14, author=message.author)
#		match = re.match('[.+] (please)?', message.content)	
#
#		if match == None:
#			await client.send_message(message.channel, "Don't waste my time mortal.")
#		elif match.group(2) != None:
#			drink = match.group(1)
#			msg = "Enjoy your {}"
#			await client.send_message(message.channel, msg.format(drink))
#		else:	
#			drink = match.group(1)
#			await client.send_message(message.channel, drink)
#			msg = "Sebby steps away and shortly comes back with a delicious {}."
#			await client.send_message(message.channel, msg.format(drink))
#			await client.send_message(message.channel, "*Sebby comes back after a couple minutes.* Did you enjoy your drink?")
#		
#			answer = await client.wait_for_message(timeout=10, author= message.author)
#			if answer == 'yes' or 'Yes':
#				msg = "*Sebby grins, then nods. He steps away with the satisfaction of knowing he %s.* " % random.choice(rude_list)
#				await client.send_message(message.channel, msg)
#			else:
#				await client.send_message(message.channel, "*Sebby nods, walking away looking quite agitated.*")