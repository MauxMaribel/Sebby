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
	
	def command_roll(self, message, command):
		match = re.match('(\d+)d(\d+) *(choose (\d+))? *(add (\d+))?', command)
		if match == None:
			self.send_message(message.channel, "I don't recognize that dice roll. Try again. :)")
		else:
			ndice = int(match.group(1))
			nfaces = int(match.group(2))
			nchoose = ndice
			if match.group(3) != None:
				nchoose = int(match.group(3))

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
			"responses": ["You roll 4d20: [0-20], [0-20], [0-20], [0-20] = [0-60]"],
			
		}
	])
