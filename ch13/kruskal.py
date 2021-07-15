from disjoint_set import DisjointSet

class Edge:
    def __init__(self, u, v, w):
        self.u=u
        self.v=v
        self.w=w

class Graph:
    def __init__(self, vertex_num):
        self.adj_list=[[] for _ in range(vertex_num)]
        self.edge_list=[]

        self.vertex_num=vertex_num

    def add_edge(self, u, v, weight):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

        self.edge_list.append(Edge(u, v, weight))

    def MST_kruskal(self):
        mst=Graph(self.vertex_num)        
        ds=DisjointSet(self.vertex_num)
        self.edge_list.sort(key=lambda e: e.w)
        mst_edge_num=0
        edge_idx=0

        while mst_edge_num < self.vertex_num-1:
            edge=self.edge_list[edge_idx]
            if ds.collapsing_find(edge.u) != ds.collapsing_find(edge.v):
                mst.add_edge(edge.u, edge.v, edge.w)
                ds.weighted_union(ds.collapsing_find(edge.u), ds.collapsing_find(edge.v))
                mst_edge_num+=1
            edge_idx+=1

        return mst

    def print_edges(self):
        for edge in self.edge_list:
            print("({}, {}) : {}".format(edge.u, edge.v, edge.w))

if __name__=="__main__":
    g=Graph(6)

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 8)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 4, 12)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 4, 17)
    g.add_edge(3, 4, 4)
    g.add_edge(3, 5, 14)

    mst=g.MST_kruskal()

    mst.print_edges()
    
