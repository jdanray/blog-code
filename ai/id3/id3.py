from math import log
from collections import Counter

# given a list of examples, each of which is composed of a set of attribute-value pairs,
# returns all of the values that a given attribute can take on
def attr_values(attribute, examples):
	return list(set(e[attribute] for e in examples))

# returns the number of bits needed to identify each class
def entropy(examples, target):
	# partition the examples by class
	classifications = [[e for e in examples if e[target] == v] for v in attr_values(target, examples)]
	
	# compute the probability that a class of example will occur
	num_examples = float(len(examples))
	proportions = [len(c) / num_examples for c in classifications]
	
	return -sum(p * log(p, 2) for p in proportions)

# returns the gain in information due to the given attribute
def info_gain(examples, attribute, target):
	# partition the examples by attribute value
	exs = [[e for e in examples if e[attribute] == v] for v in attr_values(attribute, examples)]
	
	info = entropy(examples, target)
	
	# compute conditional entropy
	num_examples = float(len(examples))
	conditional_info = sum(len(e) / num_examples * entropy(e, target) for e in exs)

	return info - conditional_info
	
# constructs the decision tree
def id3(examples, attributes, target):
	# a decision tree is of the form
	# {attribute: {value1: subtree1, value2: subtree2, ...}}
	# or it might simply be a classification
	
	# if we don't have any examples to classify,
	# then return a null classification
	if not examples:
		return ''

	# grab and count all the target attribute values
	tvals = [e[target] for e in examples]	# DON'T use attr_values()
	tcount = Counter(tvals)

	# if all of the given examples have the same classification,
	# create a leaf with that target attribute value
	if tcount[tvals[0]] == len(tvals):
		return tvals[0]
	
	# if we've run out of attributes to split on,
	# create a leaf with the target attribute value most common among the examples
	if not attributes:
		return tcount.most_common(1)[0][0]

	# split on the attribute with maximum information gain
	# now that you've used that attribute, don't include it in the subtrees
	attr = max(attributes, key=lambda a: info_gain(examples, a, target))
	new_attrs = [a for a in attributes if a is not attr]
	return {attr: {val: id3([e for e in examples if e[attr] == val], new_attrs, target) for val in attr_values(attr, examples)}}

# depth-first search through the tree to build the corresponding ruleset
def build_ruleset(tree):
	ruleset = []
	stack = [[tree, []]]
	
	while stack:
		t, rule = stack.pop()
		
		if not isinstance(t, dict):
			ruleset.append('IF ' + ' AND '.join(r[0] + ' = ' + r[1] for r in rule) + ' THEN ' + str(t))
			continue
		
		attr = list(t.keys())[0]
		for val in t[attr]:
			stack += [[t[attr][val], rule + [(attr, val)]]]
		
	return ruleset
