from id3 import id3
from collections import Counter, defaultdict

train_file = 'vote_train.txt'
test_file = 'vote_test.txt'

target = 'party'

features = ["infants", "water_share", "budget_res", "physician_fee_freeze", "aid", "religion", "satellite_ban", "contras", "missile", "immigration", "corp_cutback", "education", "sue", "crime", "exports", "africa", "party"]

def preprocess(file_location):
	examples = []
	with open(file_location, 'r') as file:
		examples = [dict(zip(features, ex.rstrip().split(','))) for ex in file]
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

def main():
	training = preprocess(train_file)
	testing = preprocess(test_file)
	attributes = [a for a in training[0].keys() if a is not target]

	tree = id3(training, attributes, target)

	results = test_tree(tree, testing, target)
	print('%f%% correct' % (results[True] * 100.0 / len(testing)))

if __name__ == "__main__":
	main()
