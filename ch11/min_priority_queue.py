from heapq import heappush, heappop

class Element:
    def __init__(self, key, string):
        self.key=key
        self.data=string

class MinPriorityQueue:
    def __init__(self):
        self.heap=[]

    def is_empty(self):
        if not self.heap:
            return True
        return False

    def push(self, item):
        heappush(self.heap, (item.key, item.data))

    def pop(self):
        return heappop(self.heap)

    def min(self):
        return self.heap[0]

if __name__=="__main__":
    pq=MinPriorityQueue()
    
    pq.push(Element(2, "kim"))
    pq.push(Element(14, "park"))
    pq.push(Element(9, "choi"))
    pq.push(Element(11, "lee"))
    pq.push(Element(6, "yang"))
    pq.push(Element(8, "jang"))

    while not pq.is_empty():
        elem=pq.pop()
        print(f"key[{elem[0]}] : data[{elem[1]}]")



    