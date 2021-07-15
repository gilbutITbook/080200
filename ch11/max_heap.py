class Element:
    def __init__(self, key):
        self.key=key

class MaxHeap:
    MAX_ELEMENTS=100
    def __init__(self):
        self.arr=[None for i in range(self.MAX_ELEMENTS+1)]
        self.heapsize=0

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

        # 완전 이진 트리를 유지하기 위해
        # 마지막 원소의 다음 인덱스
        self.heapsize+=1
        cur_idx=self.heapsize

        #cur_idx가 루트가 아니고
        #item의 key가 cur_idx 부모의 키보다 크면
        while cur_idx!=1 and item.key > self.arr[self.parent(cur_idx)].key:
            self.arr[cur_idx]=self.arr[self.parent(cur_idx)]
            cur_idx=self.parent(cur_idx)
        self.arr[cur_idx]=item

    def pop(self):
        if self.is_empty():
            return None

        #삭제된 후 반환될 원소
        rem_elem=self.arr[1]

        # 맨 마지막에 위치한 원소를 받아온 후
        # 힙 사이즈를 줄이면 완전 이진 트리 특성을 유지할 수 있다.
        temp=self.arr[self.heapsize]
        self.heapsize-=1

        #루트에서 시작
        cur_idx=1
        # 루트의 왼쪽 자식
        child = self.left(cur_idx)
    
        # 만약 child > heapsize 이면 
        # arr[cur_idx]는 리프 노드이다
        while child <= self.heapsize:
            # 오른쪽 자식이 있고
            # 오른쪽 자식의 키가 왼쪽 자식의 키보다 크면
            # child를 오른쪽 자식으로
            if child < self.heapsize and \
               self.arr[self.left(cur_idx)].key < self.arr[self.right(cur_idx)].key:
               child = self.right(cur_idx)
            # 최대 힙 특성을 만족하면 
            # 반복문을 나온다.
            if temp.key >= self.arr[child].key:
                break
            # 키가 큰 자식 원소를 부모로 이동시킨다
            # cur_idx는 자식 원소로 이동한다.
            self.arr[cur_idx]=self.arr[child]
            cur_idx=child
            child=self.left(cur_idx)
        
        self.arr[cur_idx]=temp

        return rem_elem

# 힙 내부에 있는 arr를 
# 직접 확인하기 위한 함수
def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].key), end="  ")
    print()

if __name__=="__main__":
    h=MaxHeap()

    h.push(Element(2))
    h.push(Element(14))
    h.push(Element(9))
    h.push(Element(11))
    h.push(Element(6))
    h.push(Element(8))

    print_heap(h)

    while not h.is_empty():
        rem=h.pop()
        print(f"poped item is {rem.key}")
        print_heap(h)
