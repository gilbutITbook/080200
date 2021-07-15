class Stack:
    def __init__(self):
        # 내부 표현(representation)
        # 실제로 데이터를 담을 객체는 
        # 동적 배열
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        # 맨 마지막 요소가 top
        # 동적 배열의 맨 마지막에 요소를 추가하는 것은
        # 스택의 top에 요소를 추가하는 것과 같다.
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        return self.container[-1]

if __name__=="__main__":
    s=Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while not s.empty():
        print(s.pop(), end='  ')