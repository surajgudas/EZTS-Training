stc=[]

def push_element(n):
    if(len(stc)==n):
        print("Stack is full")
    else:
        ele=input("Enter element")
        stc.append(ele)
        print(stc)
def pop_element(n):
    if(len(stc)==0):
        print("stack is empty")
    else:
        e=stc.pop()
        print(e,"removed")
        print(stc)

n=int(input("Enter the size of the stack"))
while True:
    print("select the opertaion \n1.push\n2.pop\n3.quit")
    choice=int(input())
    if(choice==1):
        push_element(n)
    elif(choice==2):
        pop_element(n)
    elif(choice==3):
        break
    else:
        print("Enter the correct operation")
    
