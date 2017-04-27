from sys import argv
from random import randint

with open('diceware.wordlist.asc') as f:
	wordlist = [word for word in f]

# roll an n-sided die nrolls times
# combine the roll outcomes into a single number
def generate_number(nsides, nrolls):
	return randint(0, nsides ** nrolls - 1)

# match a number to a word in the wordlist
def get_word(number):
	return wordlist[number].split()[1]

# given a specified number of words,
# find that many words from the wordlist
if len(argv) == 2:
	try:
		nwords = int(argv[1])
		if nwords > 0:
			print(' '.join(get_word(generate_number(6, 5)) for _ in range(nwords)))
		else:
			print('You must specify a positive number.')
	except ValueError:
		print('You must specify an integer.')
else:
	print('You must use one command-line argument.')

# example:
# python diceware.py 7
# mind stamp miami urge thing child loki
