class Environment:
	states = set()
	actions = dict()
	rewards = dict()
	transitions = dict()

	def reward(self, state, action):
		return self.rewards[state][action]

	def transition(self, state, action):
		return self.transitions[state][action]

class QLearn:
	INFINITY = 100
	discount = 0.9

	def __init__(self, env):
		self.environment = env
		self.Q = {s: {a: 0 for a in env.actions[s]} for s in env.states}

	def updateq(self, state, action):
		r = self.environment.reward(state, action)
		t = self.environment.transition(state, action)

		if self.Q[t]:
			self.Q[state][action] = r + self.discount * max(self.Q[t][a] for a in self.Q[t])
		else:
			self.Q[state][action] = r
		
	def learnq(self):
		for s in self.environment.states:
			for a in self.environment.actions[s]:
				self.updateq(s, a)

	def train(self):
		for _ in range(self.INFINITY):
			self.learnq()

	def optimal_policy(self, state):
		if self.Q[state]:
			return max(self.Q[state], key=lambda action: self.Q[state][action])
