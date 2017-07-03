from sys import argv
from tm import TuringMachine

"""
This TM determines whether a given positive integer is divisible by 4.
TM's head starts at square 0 and moves to the right until it reaches a blank square.
Then TM's head moves one square to the left. Now TM's head is over the last bit of the given number N.
If that bit is 1, then 4 does not divide N. TM enters 'NO' state and halts.
If that bit is 0, then TM moves one square to the left. Now TM's head is over the second-to-last bit of N.
If the second-to-last bit is 1, then 4 does not divide N. TM enters 'NO' state and halts.
If the second-to-last bit is 0, then 4 does divide N. TM enters 'YES' state and halts.
It is important that TM's state changes when its head moves to the left.
The new states act as a memory, so that TM knows that it's at the last or second-to-last bit.
"""

class DivisibleByFour(TuringMachine):
	def setup(self, start_position, init_tape):
		self.tape[start_position:len(init_tape)] = init_tape

		self.table['goto_end'] = {}
		self.table['goto_end'][1] = [('move', 'right')]
		self.table['goto_end'][0] = [('move', 'right')]
		self.table['goto_end'][self.blank] = [('move', 'left'), ('change_state', 'lastbit')]

		self.table['lastbit'] = {}
		self.table['lastbit'][1] = [('change_state', self.no)]
		self.table['lastbit'][0] = [('move', 'left'), ('change_state', 'secondlast')]

		self.table['secondlast'] = {}
		self.table['secondlast'][1] = [('change_state', self.no)]
		self.table['secondlast'][0] = [('change_state', self.yes)]

def main(args):
	# error-check arguments
	if len(args) != 2:
		print('You must use one command-line argument.')
		return False
	try:
		N = int(args[1])
	except ValueError:
		print('You must specify an integer.')
		return False
	if N <= 0:
		print('You must specify a positive number.')
		return False

	# turn a string-structured decimal representation
	# into a list-structured binary representation
	N = bin(N)
	N = [int(b) for b in N[2:]]

	# create, setup, and run our machine
	db4 = DivisibleByFour(init_head=0, init_state='goto_end')
	db4.setup(start_position=0, init_tape=N)
	db4.run()

	# report the TM's determination
	print(db4.state)

if __name__ == '__main__':
	main(argv)
