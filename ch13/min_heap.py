class Element:
    def __init__(self, v, w, _from):
        # 가중치를 키로 사용한다
        self.w=w
        self.v=v
        self._from=_from

class MinHeap:
    MAX_ELEMENTS=200
    def __init__(self):
        self.arr=[None for i in range(self.MAX_ELEMENTS)]
        self.heapsize=0
        #정점이 arr에 위치한 현재 인덱스
        self.pos=[None for i in range(self.MAX_ELEMENTS)]

    def is_empty(self):
        if self.heapsize==0:
            return True
        return False

    def is_full(self):
        if self.heapsize>=self.MAX_ELEMENTS:
            return True
        return False

    def parent(self, idx):
        return idx >> 1

    def left(self, idx):
        return idx << 1

    def right(self, idx):
        return (idx << 1) + 1

    def push(self, item):
        if self.is_full():
            raise IndexError("the heap is full!!")

        self.heapsize+=1
        cur_idx=self.heapsize

        while cur_idx!=1 and item.w < self.arr[self.parent(cur_idx)].w: 
            self.arr[cur_idx]=self.arr[self.parent(cur_idx)]
            # pos의 인덱스는 정점, arr는 weight를 키로 만든 최소 힙
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=self.parent(cur_idx)

        self.arr[cur_idx]=item
        self.pos[item.v]=cur_idx

    def pop(self):
        if self.is_empty():
            return None

        rem_elem=self.arr[1]

        temp=self.arr[self.heapsize]
        self.heapsize-=1

        cur_idx=1
        child=self.left(cur_idx)

        while child <= self.heapsize:
            if child < self.heapsize and \
                self.arr[self.left(cur_idx)].w > self.arr[self.right(cur_idx)].w:
                child=self.right(cur_idx)
            
            if temp.w <= self.arr[child].w:
                break

            self.arr[cur_idx]=self.arr[child]
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=child
            child=self.left(cur_idx)
        
        self.arr[cur_idx]=temp
        self.pos[temp.v]=cur_idx

        return rem_elem

    def decrease_weight(self, new_elem):
        cur=self.pos[new_elem.v]

        while cur!= 1 and new_elem.w < self.arr[self.parent(cur)].w:
            self.arr[cur]=self.arr[self.parent(cur)]
            self.pos[self.arr[cur].v]=cur    

            cur=self.parent(cur)

        self.arr[cur]=new_elem
        self.pos[new_elem.v]=cur

