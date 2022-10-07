#Linked list is a data structure which contains data objects which are connected by link. Each linked list consists of nodes which have a data field and a reference to the next node in the linked list.

##What is a node in a linked list?
#A node is an object which has a data field and a pointer to another node in the linked list. A simple structure of a node can be shown in the following figure.


#We can implement the above object using a class Node having two fields namely data and next as follows.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
        
#An empty linked list will be a linked list having its head pointer pointing to None. An empty linked list can be created in python as follows.

class linkedList:
    def __init__(self):
        self.head=None
        
        
#Inserting an element to a linked list
#We can insert an element in a linked list at the first position, in the last position on anywhere in between. 

#To insert an element in a linked list at the beginning, we will first create a node and with the given data and assign its next reference to the first node i.e where the head is pointing. Then we point the head reference to the new node.To perform this operation, we implement the method insertAtBeginning as follows.

def insertAtBeginning(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
            
            
#To insert an element in a linked list at the end, we just have to find the node where the next element refers to None i.e. the last node. Then we create a new node with the given data and point the next element of the last node to the newly created node. To perform this operation, we implement the method insertAtEnd as follows.

def insertAtEnd(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
            
            
#To insert an element at any other given position, we can count the nodes till we reach that position and then we point the next element of the new node to the next node of the current node and the next reference of the current node to the new node. This can be implemented using the insertAtGivenPosition method as follows.

def insertAtGivenPosition(self,data,position):
        count=1
        curr=self.head
        while count<position-1 and curr!=None:
            curr=curr.next
            count+=1
        temp=Node(data)
        temp.next=curr.next
        curr.next=temp
        
        
#Traversing a linked list
#To traverse a linked list in python, we will start from the head, print the data and move to the next node until we reach None i.e. end of the linked list. The following traverse() method implements the program to traverse a linked list in python.

def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
            
            
#Deleting a node
#We can delete a node either from the start or end or in between two nodes of a linked list. 

#To delete the first node of a linked list, we will first check if the head of the linked list is pointing to None, if yes then we will raise an exception using python try except with a message that the linked list is empty. Otherwise, we will delete the current node referred by head and move the head pointer to the next node. This can be implemented as follows.

def delFromBeginning(self):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                temp=self.head
                self.head=self.head.next
                del temp
        except Exception as e:
            print(str(e))
            
#To delete the last node of the linked list, we will traverse each node in the linked list and check if the next pointer of the next node of current node points to None,if yes then the next node of current node is the last node and it will get deleted. This can be implemented as follows.

def delFromEnd(self):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                curr=self.head
                prev=None
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                prev.next=curr.next
                del curr
        except Exception as e:
            print(str(e))
            
       

#To delete a node in between the linked list, at every node we will check if the position of next node is the node to be deleted, if yes, we will delete the next node and assign the next reference to the next node of the node being deleted. This can be done as follows.

def delAtPos(self,position):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                curr=self.head
                prev=None
                count=1
                while curr!=None and count<position:
                    prev=curr
                    curr=curr.next
                    count+=1
                prev.next=curr.next
                del curr
        except Exception as e:
            print(str(e))

          
#length of the linked list
def lent(self):
    c = 0
    curr=self.head
    while curr!=None:
        c+=1
        curr=curr.next
    return c
