# a reinvention of the wheel
# ...featuring my own implementation of the priority queue!

from heap import Heap

INFINITY = 100000

def dijkstra(graph, s):
    dist = {}
    for u in graph:
        dist[u] = INFINITY
    dist[s] = 0

    path = {}
    path[s] = [s]

    pq = Heap()
    pq.insert(s, dist[s])

    while not pq.empty():
        u = pq.remove()

        if u not in graph:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                path[v] = path[u] + [v]

                if pq.contains(v):
                    pq.update(v, dist[v])
                else:
                    pq.insert(v, dist[v])

    return dist, path

def main():
    graph = {'a': [['b', 5], ['c', 10]], 'b': [['c', 2]], 'c': []}
    
    start = 'a'
    dist, path = dijkstra(graph, start)
    
    end = 'c'
    print(dist[end])
    print(path[end])
    
if __name__ == "__main__":
    main()
