from queue import Queue

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

class TreeNode:
    def __init__(self, data=None):
        self.__data=data
        self.__left=None
        self.__right=None

    def __del__(self):
        print('data {} is deleted'.format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data=data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left=left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right=right

def preorder(cur):
    # 현재 노드가 empty node라면
    if not cur:
        return

    # 방문
    print(cur.data, end='  ')
    # 왼쪽 서브 트리로 이동
    preorder(cur.left)
    # 오른쪽 서브 트리로 이동
    preorder(cur.right)

def inorder(cur):
    # 현재 노드가 empty node라면
    if not cur:
        return

    # 왼쪽 서브 트리로 이동
    inorder(cur.left)
    # 방문
    print(cur.data, end='  ')
    # 오른쪽 서브 트리로 이동
    inorder(cur.right)

def postorder(cur):
    if not cur:
        return

    postorder(cur.left)
    postorder(cur.right)
    print(cur.data, end='  ')

def iter_preorder(cur):
    s=Stack()
    while True:
        while cur:
            print(cur.data, end='  ')
            s.push(cur)
            cur=cur.left

        cur=s.pop()
        if not cur:
            break

        cur=cur.right

def iter_inorder(cur):
    s=Stack()
    while True:
        while cur:
            s.push(cur)
            cur=cur.left
        cur=s.pop()
        if not cur:
            break
        # 방문을 pop을 한 이후에 합니다.
        print(cur.data, end='  ')
        cur=cur.right
            
def levelorder(cur):
    q=Queue()

    q.put(cur)
    while not q.empty():
        cur=q.get()
        print(cur.data, end='  ')

        if cur.left:
            q.put(cur.left)

        if cur.right:
            q.put(cur.right)

if __name__=="__main__":
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    n7=TreeNode(7)

    n1.left=n2; n1.right=n3
    n2.left=n4; n2.right=n5
    n3.left=n6; n3.right=n7

    # preorder(n1)
    iter_preorder(n1)
    print()

    #inorder(n1)
    iter_inorder(n1)
    print()

    postorder(n1)
    print()

    levelorder(n1)
    print()



