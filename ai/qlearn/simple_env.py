import qlearn

env = qlearn.Environment()
env.states = {0, 1, 2, 3, 4}
env.actions = {0: ['U', 'R'], 1: ['D'], 2: ['U', 'R'], 3: ['D'], 4: ['L']}
env.rewards = {0: {'U': -10, 'R': 0}, 1: {'D': 0}, 2: {'U': -10, 'R': 10}, 3: {'D': 0}, 4: {'L': 0}}
env.transitions = {0: {'R': 2, 'U': 1}, 1: {'D': 0}, 2: {'U': 3, 'R': 4}, 3: {'D': 2}, 4: {'L': 3}}

agent = qlearn.QLearn(env)
agent.train()

for s in env.states:
	print('In state %i, %s is the best action.' % (s, agent.optimal_policy(s)))
