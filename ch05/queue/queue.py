class Queue:
    def __init__(self):
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        # 동적 배열의 맨 처음 데이터를 삭제하므로
        # 빅오는 O(n)
        # 좀 더 효율적으로 구현할 수는 없을까?
        return self.container.pop(0) 

    def peek(self):
        return self.container[0]

if __name__=="__main__":
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue(), end='  ')