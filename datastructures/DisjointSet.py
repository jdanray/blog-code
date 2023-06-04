class DisjointSet:
	def __init__(self, N):
		self.id = list(range(N))
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
		if self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		if self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1

		self.id[xx] = yy
		return True
