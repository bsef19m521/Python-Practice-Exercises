# Write a python program to get size of the file using os module
import os
def GetSize(filename):
    with open(filename, 'r') as f:
        size = os.stat(filename).st_size
        return size
    
filename = input("Enter the name of the file : ")
print("Size of the file ",filename, 'is : ', GetSize(filename))
