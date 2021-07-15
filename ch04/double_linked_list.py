class Node:
    def __init__(self, data=None):
        self.__data=data
        self.__prev=None
        self.__next=None

    # 소멸자 : 객체가 사라지기 전 반드시 호출됩니다.
    # 삭제 연산 때 삭제되는 것을 확인하기 위해
    # 작성하였습니다.
    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data=data
    
    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev=p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
        self.d_size=0

    def empty(self):
        if self.d_size==0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node=Node(data)
        
        new_node.next=self.head.next
        new_node.prev=self.head

        self.head.next.prev=new_node
        self.head.next=new_node

        self.d_size+=1

    def add_last(self, data):
        new_node=Node(data)

        new_node.prev=self.tail.prev
        new_node.next=self.tail

        self.tail.prev.next=new_node
        self.tail.prev=new_node

        self.d_size+=1

    def insert_after(self, data, node):
        new_node=Node(data)

        new_node.next=node.next
        new_node.prev=node

        node.next.prev=new_node
        node.next=new_node

        self.d_size+=1

    def insert_before(self, data, node):
        new_node=Node(data)

        new_node.prev=node.prev
        new_node.next=node

        node.prev.next=new_node
        node.prev=new_node

        self.d_size+=1

    def search_forward(self, target):
        cur=self.head.next
        
        while cur is not self.tail:
            if cur.data==target:
                return cur
            cur=cur.next
        return None

    def search_backward(self, target):
        cur=self.tail.prev
        while cur is not self.head:
            if cur.data==target:
                return cur
            cur=cur.prev
        return None
        
    def delete_first(self):
        if self.empty():
            return
        self.head.next=self.head.next.next
        self.head.next.prev=self.head

        self.d_size-=1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail

        self.d_size-=1

    def delete_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

        self.d_size-=1

def show_list(dlist):
    print('data size : {}'.format(dlist.size()))
    cur=dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur=cur.next
    print()

if __name__=="__main__":
    dlist=DoubleLinkedList()
    print('*'*100)
    print('데이터 삽입 -add_first')
    # dlist.add_first(1)
    # dlist.add_first(2)
    # dlist.add_first(3)
    # dlist.add_first(5)

    print('데이터 삽입 -add_last')
    dlist.add_last(1)
    dlist.add_last(2)
    dlist.add_last(3)
    dlist.add_last(5)
    show_list(dlist)

    print('데이터 삽입 - insert_after')
    dlist.insert_after(4, dlist.search_forward(3))
    show_list(dlist)

    print('데이터 삽입 - insert_before')
    dlist.insert_before(4, dlist.search_forward(5))
    show_list(dlist)

    print('데이터 탐색')
    target=3
    #res=dlist.search_forward(target)
    res=dlist.search_backward(target)
    if res:
        print('데이터 {} 탐색 성공'.format(res.data))
    else:
        print('데이터 {} 탐색 실패'.format(target))
    res=None

    # print('데이터 삭제-delete_first')
    # dlist.delete_first()
    # dlist.delete_first()

    # print('데이터 삭제-delete_last')
    # dlist.delete_last()
    # dlist.delete_last()

    print('데이터 삭제-delete_node')
    dlist.delete_node(dlist.search_backward(5))

    show_list(dlist)

    print('*'*100)