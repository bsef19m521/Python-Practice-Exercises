# Write a python program to find the longest word from the file
def LongestWord(filename):
    # opening of  filename
    with open(filename) as f:
        data = f.read().split(' ')
        word = len(max(data,key=len))
        for i in data:
            if len(i)==word:
                print("Longest word found in file is : " + i)
        
filename =input("Enter name of the file, from where you want to find the longest word from the file : ")
LongestWord(filename)
    
    
    


