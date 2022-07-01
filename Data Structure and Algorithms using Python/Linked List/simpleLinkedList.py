# create a node class 
class Node:
    # function to initalize node object 
    def __init__(self, data):
        self.data = data    #this line assign data to the node
        self.next = None    #next/reference to the Node is null

# LinkedList is a collection of multiple nodes
# This class also contains the object of the node class  
class LinkedList:
    def __init__(self):
        self.head = None # function to initialize the head of the linkedList
    
    # this function prints content of linked list started from the head of the linkedList
    def displayList(self):
        current = self.head
        print("All the data in the linkedList is available : ")
        while current != None:
            print(current.data)
            current = current.next
        
if __name__ == '__main__':
    # start with any empty linkedList
    list1 = LinkedList()
    # First Node of the linkedList
    list1.head = Node(32)
    
    # Second Node of the linkedList
    second = Node(21)
    
    # Third Node of the linkedList
    third = Node(54)    
    # Link first Node with the second node 
    list1.head.next = second
    
    # link second node with the third node
    second.next = third
    
    print("First Node of the linkedList: " + str(list1.head.data))
    print("Second Node of the linkedList: " + str(second.data))
    print("Third Node of the linkedList: " + str(third.data))
    
    list1.displayList()
    # print(list1.head.next)
    # print(second.next)
    # print(third.next)