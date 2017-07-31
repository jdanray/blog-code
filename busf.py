# file locations
CONSTANTS_FILE = 'params/constants.txt'
TRANSITION_MODEL_FILE = 'params/transitionModel.txt'
OBSERVATION_MODEL_FILE = 'params/observationModel.txt'
PRIOR_MODEL_FILE = 'params/priorModel.txt'
NAMES_FILE = 'params/names.txt'
OBSBUSF_FILE = 'observationsTrain/obsBuSF.txt'
OBSBUSF_FILE = 'observationsTest/obsBuSF.txt'

# some constants
with open(CONSTANTS_FILE, 'r') as f:
    NUM_HORSES, NUM_BUSF, NUM_RACES = [int(line.rstrip()) for line in f]

# the horses
with open(NAMES_FILE, 'r') as f:
    HORSE_NAMES = [name.rstrip() for name in f]

# builds a matrix out of the data in a file
def build_matrix(file_location):
    with open(file_location, 'r') as f:
        m = [[float(r) for r in row.rstrip().split()] for row in f]
    return m

# the models
transition_model = build_matrix(TRANSITION_MODEL_FILE)
observation_model = build_matrix(OBSERVATION_MODEL_FILE)
prior_model = build_matrix(PRIOR_MODEL_FILE)

# the observations of each horse for each race
observations = build_matrix(OBSBUSF_FILE)

# given an observation or transition model and a prior probability distribution,
# computes a probability distribution over random variables in our horse-racing world
def predict(model, priors):
    prediction = [0.0] * NUM_BUSF
    for i in range(NUM_BUSF):
        prediction = [prediction[j] + model[i][j] * priors[i] for j in range(NUM_BUSF)]
    return prediction

# given a prediction and an observation, refines the prediction using the observation
def refine(prediction, observation):
    evidence = [observation_model[i][observation] for i in range(NUM_BUSF)]
    return [prediction[i] * evidence[i] for i in range(NUM_BUSF)]

# given a probability distribution, makes the distribution's elements sum to 1
def normalize(prediction):
    alpha = 1.0 / sum(prediction)
    return [p * alpha for p in prediction]

# for each horse, filter up to Race 24
current_BuSF = prior_model * NUM_HORSES
for t in range(NUM_RACES):
    current_BuSF = [normalize(refine(predict(transition_model, current_BuSF[h]), int(observations[t][h]))) for h in range(NUM_HORSES)]

# for each horse, predict its BuSF for Race 25
future_BuSF = [normalize(predict(transition_model, current_BuSF[h])) for h in range(NUM_HORSES)]

# for each horse, predict its obsBuSF for Race 25
future_obsBuSF = [normalize(predict(observation_model, future_BuSF[h])) for h in range(NUM_HORSES)]

# for each horse, compute its expObsBuSF for Race 25
expObsBuSF = [sum(i * future_obsBuSF[h][i] for i in range(NUM_BUSF)) for h in range(NUM_HORSES)]

# rank the horses by expObsBuSF
ranking = sorted(zip(HORSE_NAMES, expObsBuSF), key=lambda x: x[1], reverse=True)

# report the ranking
print('Predicted Finish   Horse Name     expObsBuSF')
for i, (name, eobusf) in enumerate(ranking):
    print(' '.ljust(6) + str(i + 1).ljust(13) + name.ljust(15) + str(eobusf))
