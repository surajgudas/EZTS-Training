class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp):
                if(temp.next==None):
                    print(temp.data)
                else:
                    print(temp.data,"->",end="")
                temp=temp.next
    def insert_beginning(self):
        new_node=Node(50)
        new_node.next=self.head
        self.head=new_node
    def add_last(self):
        new_node=Node(60)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node
    def add_middle(self):
        new_node=Node(25)
        temp=self.head
        '''
        while(temp.data!=20):
            temp=temp.next
        '''
        n=3
        for i in range(n-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def del_last(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def del_beg(self):
        temp=self.head
        self.head=temp.next
    def del_mid(self):
        temp=self.head
        '''
        while(temp.next.data!=25):
            temp=temp.next
        '''
        k=3
        for i in range(k-2):
            temp=temp.next
        temp.next=temp.next.next
    def circular(self):
        l1=[]
        z=0
        temp=self.head
        while(temp.next!=self.head):
            if(temp.next in l1):
                z=1
                print("True")
                break
            l1.append(temp)
            temp=temp.next
        if(temp.next in l1):
            print("True")
            z=1
        if(z==0):
            print("False")
        
obj=Sll()

node_1=Node(10)
obj.head=node_1

node_2=Node(20)
node_1.next=node_2

node_3=Node(30)
node_2.next=node_3

node_4=Node(40)
node_3.next=node_4

obj.display()

obj.insert_beginning()
obj.display()

obj.add_last()
obj.display()

obj.add_middle()
obj.display()

obj.del_last()
obj.display()

obj.del_beg()
obj.display()

obj.del_mid()

obj.display()

obj.circular()
