from heapq import heappush, heappop 

class MinPriorityQueue:
    def __init__(self):
        self.heap=[]
    
    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

class ShortestPath:
    def __init__(self, s, distance, p):
        self.source=s
        self.distance=distance
        self.p=p

    def print_shortest_path(self, dest):
        if self.source==dest:
            print(dest, end="  ")
            return
        if sp.p[dest]!=None:
            self.print_shortest_path(self.p[dest])
        else:
            print("There is no path")
            return
        print(dest, end="  ")

class Graph:
    #모든 가중치보다 충분히 큰 수
    BIG_NUMBER=2000
    def __init__(self, vertex_num):
        self.adj_matrix=[[None for _ in range(vertex_num)] for _ in range(vertex_num)]
        self.vertex_num=vertex_num

    def add_edge(self, u, v, w):
        self.adj_matrix[u][v]=w

    def dijkstra(self, s):
        distance=[self.BIG_NUMBER for _ in range(self.vertex_num)]
        p=[None for _ in range(self.vertex_num)]

        S=set()
        pq=MinPriorityQueue()
        for i in range(self.vertex_num):
            pq.push((self.BIG_NUMBER, i))

        distance[s]=0
        pq.push((0, s))        

        while len(S) < self.vertex_num:
            d, v = pq.pop()
            if distance[v] != d:
                continue

            S.add(v)

            adj_v = self.adjacent_set(v)
            for u, w_u_v in adj_v:
                if u not in S and distance[u] > distance[v]+w_u_v:
                    distance[u]=distance[v]+w_u_v
                    p[u]=v
                    pq.push((distance[u], u))
            
        sp=ShortestPath(s, distance, p)
        return sp

    def adjacent_set(self, v):
        adj_v=[]
        for i in range(self.vertex_num):
            w=self.adj_matrix[v][i]
            if w:
                adj_v.append((i, w))
        return adj_v

if __name__=="__main__":
    g=Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 1, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 1, 4)
    g.add_edge(3, 2, 12)

    source=0
    sp=g.dijkstra(source)
    for i in range(g.vertex_num):
        print(f"distance[{i}] : {sp.distance[i]}, p[{i}] : {sp.p[i]}")
    
    dest=3
    print(f"path from {source} to {dest}")
    sp.print_shortest_path(dest)
    print()

