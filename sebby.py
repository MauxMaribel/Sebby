import sys
import re
import random
import spells

rude_list = ['spit in your drink', 'licked the rim of the glass', 'used a dirty glass', 'dunked a roach in the drink']

class Sebby:

	def send_message(self, channel, msg):
		print("Sending to %s: %s", channel, msg)

	
	def handle_message(self, message):
		match = re.match('!([a-zA-Z]+) *(.*)', message.content)

		if match == None:
			return

		#this little bit of magic lets us just define functions in
		#this class with the name of the command and handle them.
		message_type = match.group(1).lower()
		handler = self.__getattribute__('command_' + message_type)
		if handler != None:
			handler(message, match.group(2))

	def command_test(self, message, command):
		self.send_message(message.channel, "Responding to test")

	def command_spank(self, message, command):
		self.send_message(message.channel, "*Sebby turns Vexi across his knee and starts spanking her!!!*")
		
	def command_makeitbetter(self, message, command):
		self.send_message(message.channel, "*gives you a big hug*")
	
	def command_makeitworse(self, message, command):
		self.send_message(message.channel, "*mocks Vexi mercilessly*")
		
	def command_thankyou(self, message, command):
		author = message.author
		msg = "You're very welcome {}"
		self.send_message(message.channel, msg.format(author))
		
	def command_report(self, message, command):
		self.send_message(message.channel, "Sorry. You can't report her yet. Soon though. Very soon she will recieve severe punishments because of you.")
	
	def command_suggest(self, message, command):
		self.send_message(message.channel, "Sorry. Can't give suggestions this way yet.")
	
	def command_roll(self, message, command):
		match = re.match('(\d+)d(\d+) *(choose (\d+))? *(add (-?(\d+)))?', command)
		if match == None:
			self.send_message(message.channel, "I don't recognize that dice roll. Try again. :)")
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

			self.send_message(message.channel, "You roll %dd%d: %s = %d" % (ndice, nfaces, msg, total))
			
	def command_help(self, message, command):
		msg = """Pathfinder Related:
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
		self.send_message(message.channel, msg)
		
	def command_listspells(self, message, command):
		match = re.match('(.+) (\d+)', command)
		temp_list = []
		pclass = match.group(1)
		level = int(match.group(2))
		temp_list.append(pclass)
		class_list = spells.find_class_spells(temp_list[0], level)
		
		if class_list == []:
			self.send_message(message.channel, "I do not have any information for that. Try again.")
		else:
			msg = "You asked about %s level %d spells." % (temp_list[0], level)
			self.send_message(message.channel, msg)
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
					self.send_message(message.channel, result1)
					self.send_message(message.channel, result2)
					self.send_message(message.channel, result3)
				else:
					self.send_message(message.channel, result1)
					self.send_message(message.channel, result2)
			else:
				self.send_message(message.channel, result)
	
	def command_spellinfo(self, message, command):
		spell = message.content[11:]
		
		answer = spells.find_by_name(spell)
		if answer == None:
			self.send_message(message.channel, "Sorry, that is not a valid spell. Try again.")
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
			self.send_message(message.channel, msg)
			self.send_message(message.channel, msg2)

class TestMessage:
	content = ''
	channel = '#test'

class TestSebby(Sebby):
	failed = False
	expected_messages = []
	expected_responses = []
	def send_message(self, channel, msg):
		if self.expected_responses == []:
			self.failed = True
			return

		if re.match(self.expected_responses[0], msg) == None:
			print("WRONG RESPONSE: %s INSTEAD OF %s" % (msg, self.expected_responses[0]))
			self.failed = True
			return

		self.expected_responses = self.expected_responses[1:]
	
	def run_tests(self):
		for msg in self.expected_messages:
			self.expected_responses = msg['responses']
			message = TestMessage()
			message.content = msg['message']
			self.handle_message(message)
			if self.expected_responses != []:
				print("ERROR: EXPECTED A RESPONSE %s AND DIDN'T GET IT" % self.expected_responses[0])
				return False
			if self.failed:
				return False

		return not self.failed


def run_sebby_test(name, tests):
	print("Running test", name)
	test_bot = TestSebby()
	test_bot.expected_messages = tests
	result = test_bot.run_tests()
	if result:
		print("Test", name, "PASSED!")
	else:
		print("Test", name, "FAILED!")

if __name__ == '__main__':
	run_sebby_test("test", [
		{
			"message": "!test",
			"responses": ["Responding to test"],
		}
	])

	run_sebby_test("spank", [
		{
			"message": "!spank",
			"responses": ["\*Sebby turns Vexi across his knee and starts spanking her!!!\*"],
		}
	])

	run_sebby_test("roll", [
		{
			"message": "!roll 1d6",
			"responses": ["You roll 1d6: [0-9] = [0-9]"],
		}
	])

	run_sebby_test("roll", [
		{
			"message": "!roll 4d20 choose 3",
			"responses": ["You roll 4d20: [0-9]{1,2}, [0-9]{1,2}, [0-9]{1,2}, [0-9]{1,2} = [0-9]{1,2}"],
			
		}
	])
	
	run_sebby_test("roll", [
		{
			"message": "!roll 1d6 add 20",
			"responses": ["You roll 1d6: [0-9] \+ [0-9]{1,2} = [0-9]{1,2}"],
			
		}
	])
	
	run_sebby_test("roll", [
		{
			"message": "!roll 2d6 choose 1 add -1",
			"responses": ["You roll 2d6: [0-9], [0-9] \+ -[0-9] = [0-9]"],
		}
	])
	

