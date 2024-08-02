class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Csll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp.next!=self.head):
                print(temp.data,"->",end="")
                temp=temp.next
            print(temp.data,"->",end="")
            temp=temp.next
            print(temp.data)
        '''
        temp=self.head
        z=temp
        while(temp.next!=z):
            print(temp.data,"->",end="")
            temp=temp.next
        print(temp.data)
        '''
    def insert_beg(self,z):
        new_node=Node(z)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            start=self.head
            new_node.next=start
            self.head=new_node
            self.tail.next=self.head
    def insert_last(self,z):
        new_node=Node(z)
        temp=self.head
        while(temp!=self.tail):
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.tail=new_node
    def insert_mid(self,pos,z):
        new_node=Node(z)
        n=pos
        temp=self.head
        for i in range(n-1):
            temp=temp.next
        print(temp.data)
        if(n==1):
            obj.insert_beg(z)
        elif(temp.next==self.head):
            obj.insert_last(z)
        else:
            temp=self.head
            '''
            while(temp.data!=20):
                temp=temp.next
            '''
            for i in range(n-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def del_last(self):
        temp=self.head
        while(temp.next!=self.tail):
            temp=temp.next
        print(temp.data)
        temp.next=self.head
        self.tail=temp
    def del_beg(self):
        self.tail.next=self.head.next
        self.head=self.head.next
    def del_mid(self,pos):
        n=pos
        temp=self.head
        for i in range(n):
            temp=temp.next
        print(temp.data)
        if(n==1):
            obj.del_beg()
        elif(temp.next==self.head):
            obj.del_last()
        else:
            temp=self.head
            '''
            while(temp.next.data!=25):
                temp=temp.next
            '''
            for i in range(n-2):
                temp=temp.next
            temp.next=temp.next.next
    def circular(self):
        l1=[]
        z=0
        temp=self.head
        while(temp.next!=self.head):
            if(temp.next in l1):
                print("temp.next=",temp.next)
                print(l1)
                z=1
                print("True")
                break
            print("temp.next=",temp.next)
            print(l1)
            l1.append(temp)
            temp=temp.next
        if(temp.next in l1):
            print("temp.next=",temp.next)
            print(l1)
            print("True")
            z=1
        if(z==0):
            print("False")
    def length(self):
        z=0
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp.next!=self.head):
                z+=1
                temp=temp.next
            print("length=",z+1)
        
        

obj=Csll()

node_1=Node(10)
obj.head=node_1

node_2=Node(20)
node_1.next=node_2

node_3=Node(30)
node_2.next=node_3

node_4=Node(40)
node_3.next=node_4
obj.tail=node_4

obj.tail.next=obj.head

obj.display()

obj.insert_beg(5)
obj.display()

obj.insert_last(50)
obj.display()

obj.insert_mid(3,25)
obj.display()

obj.del_last()
obj.display()

obj.del_beg()
obj.display()

obj.del_mid(3)
obj.display()

obj.length()

obj.insert_mid(1,1)
obj.display()

obj.insert_mid(5,100)
obj.display()

obj.del_mid(1)
obj.display()

obj.del_mid(5)
obj.display()
