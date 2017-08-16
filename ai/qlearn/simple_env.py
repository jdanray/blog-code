# In the initial state (State 0), you have two actions available: U and R
# U rewards you +10 and takes you to State 2, where you have no more actions
# R costs you -100 and takes you to State 1
# BUT, in State 1, you can choose R again, which will reward you +122.333333
# So, even though U gives you +10 and R,R costs you -100,
# your optimal action sequence is not U, but R,R, because R,R nets you 10.1 in the end

import qlearn

env = qlearn.Environment()
env.states = {0, 1, 2, 3}
env.actions = {0: ['U', 'R'], 1: ['R'], 2: [], 3: []}
env.rewards = {0: {'U': 10, 'R': -100}, 1: {'R': 122 + 1/3}, 2: {}, 3: {}}
env.transitions = {0: {'R': 1, 'U': 2}, 1: {'R': 3}, 2: {}, 3: {}}

agent = qlearn.QLearn(env)
agent.train()

for s in env.states:
	action = agent.optimal_policy(s)
	if action:
		print('In state %i, %s is the best action, and you transition to state %i.' % (s, action, agent.environment.transition(s, action)))
	else:
		print('In state %i, you have no actions available.' % (s))
