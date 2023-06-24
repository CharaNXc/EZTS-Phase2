#creating node declaration & defination
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SLL:
        def __init__(self):
                    self.head=None
        def display(self):
            
            if self.head is None:
                print("linked list is empty")
            else:
                temp=self.head#temp=first node
                while temp:
                    print(temp.data,end=" ")
                    if(temp.next is not None):
                          print("->",end=" ")
                    #temp.data means first nodes data
                    temp=temp.next#establishing link
                
            
obj=SLL()
#node creation - initialising
n=node(10)#so n.data in Node class will be 10
obj.head=n #assigning first node as head
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
