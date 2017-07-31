import numpy as np

nhorses, nbusfs, nraces = map(int, np.loadtxt('params/constants.txt'))
trans_model = np.loadtxt('params/transitionModel.txt')
obs_model = np.loadtxt('params/observationModel.txt')
prior_model = np.loadtxt('params/priorModel.txt')

obsbusf_file = 'observationsTrain/obsBuSF.txt'
obsbusf_file = 'observationsTest/obsBuSF.txt'
observations = np.loadtxt(obsbusf_file)

# filter up to race 24
busf = np.tile(prior_model, (nhorses, 1))
for t in range(nraces):
	for h in range(nhorses):
		obs = int(observations[t][h])
		O = np.diag([obs_model[i][obs] for i in range(nbusfs)])
		busf[h] = O.dot(trans_model.T.dot(busf[h]))

# predict BuSF for race 25
busf = [trans_model.T.dot(busf[h]) for h in range(nhorses)]

# predict observed BuSF for race 25 and normalize
obs_busf = [obs_model.dot(busf[h]) for h in range(nhorses)]
obs_busf = [obs_busf[h] / sum(obs_busf[h]) for h in range(nhorses)]

# compute expected observed BuSF for race 25
exp_obs_busf = [sum(i * obs_busf[h][i] for i in range(nbusfs)) for h in range(nhorses)]

# rank the horses by expected observed BuSF
with open('params/names.txt', 'r') as f:
	ranking = sorted(zip([name.rstrip() for name in f], exp_obs_busf), key=lambda x: x[1], reverse=True)

# report the ranking
print('Predicted Finish   Horse Name     expObsBuSF')
for i, (name, eobusf) in enumerate(ranking):
	print(' '.ljust(6) + str(i + 1).ljust(13) + name.ljust(15) + str(eobusf))
