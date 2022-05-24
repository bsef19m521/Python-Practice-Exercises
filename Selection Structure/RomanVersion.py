# Here write your answer
def RomanNumerals(num):
    if num==1:
        print(f"Roman version of {num} is : I.")
    elif num==2:
        print(f"Roman version of {num} is : II.")
    elif num==3:
        print(f"Roman version of {num} is : III")
    elif num==4:
        print(f"Roman version of {num} is : IV")
    elif  num==5:
        print(f"Roman version of {num} is : V")
    elif num==6:
        print(f"Roman version of {num} is : VI")
    elif num==7:
        print(f"Roman version of {num} is :VII")
    elif num==8:
        print(f"Roman version of {num} is : VIII")
    elif num==9:
        print(f"Roman version of {num} is : IX")
    elif num==10:
        print(f"Roman Version of {num} is : X")
    else:
        print(f"Error! Number entered by user is out of range!")
def main():
    try:
        number =int(input("Enter a number to check its roman version : "))
        RomanNumerals(number)
    except:
        print("Invalid Input!")
        
main()