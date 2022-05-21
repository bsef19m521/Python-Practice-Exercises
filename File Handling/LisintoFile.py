# Write a Python program to write a list content to a file name "list.txt"
def ListIntoFIle(list1):
    with open("list.txt", 'w') as file:
        for i in list1:
            file.write(i)
            file.write('\n')
    with open("list.txt", 'r') as file1:
        print("Content of the file after adding list into file is : ")
        print(file1.read())
# list1 = [""]
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# calling of function
ListIntoFIle(color)
