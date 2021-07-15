class DisjointSet:
    def __init__(self, vnum):
        self.parent=[-1 for _ in range(vnum)]

    def simple_find(self, i):
        while self.parent[i] >= 0:
            i=self.parent[i]
        return i

    def simple_union(self, i, j):
        self.parent[i]=j

    def collapsing_find(self, i):
        root=trail=lead=None
        # 루트를 찾는다.
        root=i
        while self.parent[root] >= 0:
            root=self.parent[root]

        # 모든 노드를 루트의 자식으로 만든다
        trail=i
        while trail != root:
            lead=self.parent[trail]
            self.parent[trail]=root
            trail=lead

        return root

    def weighted_union(self, i, j):
        """
        paremeters i, j must be roots!
        if size[i] < size[j] then parent[i]=j
        """
        #abs(parent[i])=size[i]
        #temp_cnt는 음수이고 size[i] + size[j]
        temp_cnt=self.parent[i]+self.parent[j]

        #size[i] < size[j]
        if self.parent[i] > self.parent[j]:
            self.parent[i]=j
            self.parent[j]=temp_cnt
        #size[i] > size[j]
        else:
            self.parent[j]=i
            self.parent[i]=temp_cnt

if __name__=="__main__":
    ds=DisjointSet(5)

    # ds.simple_union(1, 2)
    # ds.simple_union(4, 2)
    # ds.simple_union(3, 0)
    # print(ds.parent)
    
    # for i in range(5):
    #     print("parent[{}] : {}".format(i, ds.simple_find(i)))

    ds=DisjointSet(5)
    ds.parent[2]=-5
    ds.parent[4]=2
    ds.parent[0]=4
    ds.parent[1]=0
    ds.parent[3]=1
    print(ds.parent)
    print("the root is {}".format(ds.collapsing_find(3)))
    print(ds.parent)