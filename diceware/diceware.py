from sys import argv
from random import randint

with open('diceware.wordlist.asc') as wordfile:
	wordlist = [word for word in wordfile]

# roll an n-sided die nrolls times
# combine the roll outcomes into a single number
def generate_number(nsides, nrolls):
	return randint(0, nsides ** nrolls - 1)

# match a number to a word in the wordlist
def get_word(number):
	return wordlist[number].split()[1]

# given a specified number of words,
# find that many words from the wordlist
def main(args):
	if len(args) != 2:
		print('You must use one command-line argument.')
		return False

	try:
		nwords = int(args[1])
	except ValueError:
		print('You must specify an integer.')
		return False

	if nwords <= 0:
		print('You must specify a positive number.')
		return False
	
	print(' '.join(get_word(generate_number(6, 5)) for _ in range(nwords)))
	return True

if __name__ == '__main__':
	main(argv)

# example:
# python diceware.py 7
# mind stamp miami urge thing child loki
