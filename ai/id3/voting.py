from id3 import id3
from collections import Counter

def preprocess(file_location):
	examples = []
	with open(file_location, 'r') as f:
		for example in f:
			infants, water_share, budget_res, physician_fee_freeze, aid, \
			religion, satellite_ban, contras, missile, immigration, \
			corp_cutback, education, sue, crime, exports, africa, party = example.rstrip().split(',')
			
			examples.append({'infants': infants, 'water_share': water_share, \
			'budget_res': budget_res, 'physician_fee_freeze': physician_fee_freeze, \
			'aid': aid, 'religion': religion, 'satellite_ban': satellite_ban, \
			'contras': contras, 'missile': missile, 'immigration': immigration, \
			'corp_cutback': corp_cutback, 'education': education, 'sue': sue, 'crime': crime, \
			'exports': exports, 'africa': africa, 'party': party})
			
	return examples

# given a list of test examples, the target attribute, and a decision tree,
# returns a count of correct and incorrect classifications
def test_tree(tree, examples, target):
	def classify(example, tree):		
		while isinstance(tree, dict):
			attr = list(tree.keys())[0]
			attr_val = example[attr]	
			if attr_val not in tree[attr]:
				c = Counter([e[attr] for e in examples])
				attr_val = c.most_common(1)[0][0]
			tree = tree[attr][attr_val]			
		return tree
	
	return Counter([classify(e, tree) == e[target] for e in examples])

train_file = 'vote_train.txt'
training = preprocess(train_file)

test_file = 'vote_test.txt'
testing = preprocess(test_file)

target = 'party'
attributes = [a for a in training[0].keys() if a is not target]

tree = id3(training, attributes, target)

results = test_tree(tree, testing, target)
print('%f%% correct' % (results[True] * 100.0 / len(testing)))
