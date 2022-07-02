from ast import While
from hashlib import new
from secrets import choice
from time import perf_counter
from tkinter import W
from traceback import print_list
from xml.dom.expatbuilder import InternalSubsetExtractor


# In linked list, we perform insertion in three ways 
# 1 -> Insertion at the beginning of the list
# 2 -> Insertion at the end of the list
# 3 -> Insertion at the any point of the list

# create a node class
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def insertatbegin(self, new_data):
        # allocate a new node and put data 
        new_node = Node(new_data)
        
        # make new node next as head 
        new_node.next = self.head
        
        # move head to point to the new node
        self.head = new_node
        
    def insertatend(self, new_data):
        # allocate a new node and put data
        new_node = Node(new_data)
        
        curr = self.head
        # If LL is empty , then make new node as first node of linked list 
        if self.head == None:
            self.head = new_node
            return
        
        # travser the list to reach end point of the linked list
        
        while curr.next:
            curr = curr.next
            
        # After reaching at the end of the linked list, the  change the next of the last node 
        curr.next = new_node
    
    def printlist(self):
        curr = self.head
        if curr == None:
            print("Nothing in the list")
        else:
            print("Elements in the linked list : ")
            while curr !=None:
                print(curr.data, sep=" ")
                curr = curr.next
                
    def listlength(self):
        curr = self.head
        count = 0
        while curr != None:
            count = count+1
            curr = curr.next
        print("Length of the linked list : ", count)
        
    def maxElement(self):
        curr = self.head
        if self.head == None:
            print("The list is empty")
        else:
            maxValue  = self.head.data
            while  curr != None:
                if maxValue < curr.data:
                    maxValue = curr.data
                curr = curr.next
            print("The maximum element is of the linked list is :" , maxValue)
            
    def minElement(self):
        curr = self.head
        if self.head == None:
            print("The list is empty")
        else:
            minValue = self.head.data
            while curr != None:
                if minValue > curr.data:
                    minValue = curr.data
                curr = curr.next
            print("The minimum element is of the linked list is :" , minValue)
    
    
    
if __name__ == '__main__':
    list1 = LinkedList()
    while True:
        choice = int(input(
        """
        1.Enter to insert a node at the beginning of the list \n
        2.Enter to insert a node at the end of the list \n
        3.Enter to insert a node given position in the list \n
        4.Enter to print all the nodes of the linked list \n
        5.Enter to print length of the linked list \n
        6.Enter to print maximum node element of the linked list \n
        7.Enter to print minimum node element of the linked list \n
        8.Enter to exit program\n
        """
        ))
        if choice==1:
            value = int(input("Enter value of node to insert at the beginning of the linked list: "))
            list1.insertatbegin(value)

        if choice==2:
            value = int(input("Enter value of node to insert at the end of the linked list: "))
            list1.insertatend(value)
        if choice==4:
            list1.printlist()
            
        if choice==5:
            list1.listlength()
        
        if choice==6:
            list1.maxElement()
        
        if choice==7:
            list1.minElement()
            
        if choice==8:
            break