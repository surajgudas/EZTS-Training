class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Dll:
    def __init__(self):
        self.head=None
    def display(self):
        print("Elements are :")
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp):
                if(temp.next==None):
                    print(temp.data)
                else:
                    print(temp.data,"<-->",end="")
                temp=temp.next
    def add_beg(self):
        print("Insert at begining")
        new_node=Node(5)
        new_node.next=self.head
        self.prev=new_node
        self.head=new_node
    def add_last(self):
        print("Insert at last")
        temp=self.head
        new_node=Node(50)
        while(temp.next):
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def add_mid(self,pos):
        print("Insert at middle")
        new_node=Node(25)
        temp=self.head
        '''
        while(temp.data!=20):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
        '''
        for i in range(pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
    def del_beg(self):
        print("Deletion at beginging")
        temp=self.head
        temp.next.prev=None
        self.head=temp.next
    def del_last(self):
        print("Deletion at last")
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def del_mid(self,pos):
        print("Deletion at middle")
        temp=self.head
        '''
        while(temp.next.data!=25):
            temp=temp.next
        z=temp.next.next
        temp.next=z
        z.prev=temp
        '''
        for i in range(pos-2):
            temp=temp.next
        z=temp.next.next
        temp.next=z
        z.prev=temp
    def db(self):
        print("Elements are :")
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            while(temp):
                if(temp.prev==None):
                    print(temp.data)
                else:
                    print(temp.data,"<-->",end="")
                temp=temp.prev
        
obj=Dll()

node_1=Node(10)
obj.head=node_1

node_2=Node(20)
node_1.next=node_2
node_2.prev=node_1

node_3=Node(30)
node_2.next=node_3
node_3.prev=node_2

node_4=Node(40)
node_3.next=node_4
node_4.prev=node_3

obj.display()

obj.add_beg()
obj.display()

obj.add_last()
obj.display()

obj.add_mid(3)
obj.display()

obj.del_beg()
obj.display()

obj.del_last()
obj.display()

obj.del_mid(3)
obj.display()

obj.db()
