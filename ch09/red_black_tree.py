class RBNode:
    def __init__(self, key):
        #트리 내에서 유일한 키
        self.key=key
        #노드의 색 : RED or BLACK
        #트리에 insert 연산을 할 때 먼저 새 노드의 색은 RED로 한다.
        self.color="RED"
        
        self.left=None
        self.right=None

        #부모
        self.parent=None

    def __str__(self):
        return str(self.key)

class RedBlackTree:
    def __init__(self):
        self.__root=None
        # 모든 외부 노드를 하나의 객체로 표현
        self.__EXT = RBNode(None)
        # 외부 노드의 컬러는 블랙
        self.__EXT.color="BLACK"

    def get_root(self):
        return self.__root

    def preorder_traverse(self, cur, func, *args, **kwargs):
        if cur == self.__EXT:
            return

        func(cur, *args, **kwargs)
        self.preorder_traverse(cur.left, func, *args, **kwargs)
        self.preorder_traverse(cur.right, func, *args, **kwargs)

    def __left_rotate(self, n):
        #n's right child
        r=n.right
        #r's left child
        l=r.left

        #l을 n의 오른쪽 자식으로
        l.parent=n
        n.right=l

        #n.parent를 r.parent로
        #n이 루트라면, 트리 루트도 업데이트
        if n==self.__root:
            self.__root=r
        elif n.parent.left==n:
            n.parent.left=r
        else:
            n.parent.right=r
        r.parent=n.parent

        #n을 r의 왼쪽 자식으로
        r.left=n
        n.parent=r

    def __right_rotate(self, n):
        #n's left child
        l=n.left
        #lc's right child
        r=l.right

        #r을 n의 왼쪽 자식으로
        r.parent=n
        n.left=r

        #n.parent를 l.parent로
        #n이 루트라면 트리의 루트도 업데이트
        if n==self.__root:
            self.__root=l
        elif n.parent.left==n:
            n.parent.left=l
        else:
            n.parent.right=l
        l.parent=n.parent

        #n을 lc의 오른쪽 자식으로
        l.right=n
        n.parent=l

    def __insert_fix(self, n): 
        pn=gn=un=None

        pn=n.parent
        while pn != None and pn.color=="RED":
            gn=pn.parent
            if gn.left==pn:
                un=gn.right
                
                if un.color=="RED":
                    gn.color="RED"
                    pn.color=un.color="BLACK"

                    n=gn
                    pn=n.parent
                    
                else:
                    if pn.right==n:
                        self.__left_rotate(pn)
                        n, pn = pn, n
                    pn.color, gn.color=gn.color, pn.color

                    self.__right_rotate(gn)
            else:
                un=gn.left
                if un.color=="RED":
                    gn.color="RED"
                    pn.color=un.color="BLACK"

                    n=gn
                    pn=n.parent
                else:
                    if pn.left==n:
                        self.__right_rotate(pn)
                        n, pn = pn, n
                    pn.color, gn.color=gn.color, pn.color
                    self.__left_rotate(gn)

        self.__root.color="BLACK"

    def insert(self, key):
        new_node=RBNode(key)
        new_node.left=self.__EXT
        new_node.right=self.__EXT

        cur=self.__root
        if not cur:
            self.__root=new_node
            #루트 노드는 BLACK
            self.__root.color="BLACK"
            return

        while True:
            parent=cur
            if key < cur.key:
                cur=cur.left
                if cur==self.__EXT:
                    parent.left=new_node
                    #노드의 parent 설정
                    new_node.parent=parent
                    break
            else:
                cur=cur.right
                if cur==self.__EXT:
                    parent.right=new_node
                    #노드의 parent 설정
                    new_node.parent=parent
                    break
        #노드 삽입 후 처리
        self.__insert_fix(new_node)

    # 편의 함수
    def print_node(self, rbn):
        if rbn:
            print("node : {}, ".format(rbn.key), end="")
            if rbn.color=="RED":
                print("color : RED, ", end="")
            else:
                print("color : BLACK, ", end="")
            if rbn.left:
                print("left : {}, ".format(rbn.left.key), end="")
            if rbn.right:
                print("right : {}, ".format(rbn.right.key), end="")
            if rbn.parent:
                print("parent : {}".format(rbn.parent.key), end="")
            print()

if __name__=="__main__":
    print('*'*100)
    rbt=RedBlackTree()
	
    for i in range(10):
	     rbt.insert(i)

    rbt.preorder_traverse(rbt.get_root(), rbt.print_node)
    print('*'*100)
