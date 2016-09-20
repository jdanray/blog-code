class TrieNode(object):
	def __init__(self):
		self.edges = dict()
		self.leaf = False
		
class Trie(object):
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
			if letter in curr.edges:
				curr = curr.edges[letter]
			else:
				return False
				
		return curr.leaf

	def startsWith(self, prefix):
		curr = self.root
		for letter in prefix:
			if letter in curr.edges:
				curr = curr.edges[letter]
			else:
				return False
				
		return True
