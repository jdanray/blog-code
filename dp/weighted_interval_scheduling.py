class Job:
    def __init__(self, start, finish, value):
        self.start  = start
        self.finish = finish
        self.value  = value

def bsearch(jobs, start_index):
    lo = 0
    hi = start_index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if jobs[mid].finish <= jobs[start_index].start:
            if jobs[mid + 1].finish <= jobs[start_index].start:
                lo = mid + 1
            else:
                return mid + 1
        else:
            hi = mid - 1			
    return 0

def schedule(jobs):
	jobs = sorted(jobs, key=lambda j: j.finish)
	n = len(jobs)
	V = [0 for _ in range(n + 1)]
	V[0] = 0
	for i in range(1, n + 1):
		p = bsearch(jobs, i - 1)
		V[i] = max(jobs[i - 1].value + V[p], V[i - 1])
	return V[n]
	
jobs = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)]
print schedule(jobs)
