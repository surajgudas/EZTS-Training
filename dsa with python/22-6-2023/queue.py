queue=[]

def enqueue(n):
    if(len(queue)==n):
        print("Queue is full")
    else:
        ele=input("Enter element")
        queue.append(ele)
        print(queue)

def dequeue(n):
    if(len(queue)==0):
        print("queue is empty")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)

n=int(input("Enter the size of the queue"))
while True:
    print("select the opertaion \n1.Enqueue\n2.Dequeue\n3.quit")
    choice=int(input())
    if(choice==1):
        enqueue(n)
    elif(choice==2):
        dequeue(n)
    elif(choice==3):
        break
    else:
        print("Enter the correct operation")
