class TuringMachine:
	def __init__(self, init_head, init_state):
		self.nsquares = 100
		self.blank = 'BLANK'
		self.yes = 'YES'
		self.no = 'NO'
		self.tape = [self.blank for _ in range(self.nsquares)]
		self.table = {}

		self.head = init_head
		self.state = init_state	

	def write(self, symbol):
		self.tape[self.head] = symbol

	def change_state(self, new_state):
		self.state = new_state

	def move(self, direction):
		if direction == 'right' and self.head < len(self.tape):
			self.head += 1
		elif direction == 'left' and self.head > 0:
			self.head -=1

	def run(self):
		while self.state != self.yes and self.state != self.no:
			curr_square = self.tape[self.head]
			for action, obj in self.table[self.state][curr_square]:
				getattr(self, action)(obj)
