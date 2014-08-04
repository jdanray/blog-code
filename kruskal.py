class Edge:
	self.u = 0
	self.v = 0
	self.w = 0

class DisjointSet:
	def __init__(self, N):
		self.id = range(N)
		self.rank = [1] * N

	def find(self, x):
		if self.id[x] != self.id[self.id[x]]:
			self.id[x] = self.find(self.id[x])
		return self.id[x]

	def union(self, x, y):
		xx = self.find(x)
		yy = self.find(y)
		if xx == yy:
			return False
		elif self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		elif self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1
		self.id[xx] = yy
		return True

"edges is a list of objects of class Edge"
"n is the number of the graph's vertices"
"m is the number of the graph's edges"
function kruskal(edges, n, m):
	uf = DisjointSet(n)
	trees = []
	for e in sorted(edges, key=lambda x: x.w): 
		uf.union(e.u, e.v) and trees.append(e)
	return trees
