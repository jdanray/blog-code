class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False
		
class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				curr.edges[letter] = TrieNode()
			curr = curr.edges[letter]
		curr.leaf = True

	def search(self, word):
		curr = self.root
		for letter in word:
			if letter not in curr.edges:
				return False
			curr = curr.edges[letter]
		return curr.leaf

	def startsWith(self, prefix):
		curr = self.root
		for letter in prefix:
			if letter not in curr.edges:
				return False
			curr = curr.edges[letter]
		return True
