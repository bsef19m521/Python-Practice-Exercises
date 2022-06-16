# In this program , we toss a coin and return head or tail to the user 
import random
class Coin:
    def __init__(self):
        self.__sideup = 'Head'
        
    def toss(self):
        if random.randint(0,1)==0:
            self.__sideup = 'Head'
        else:
            self.__sideup = 'Tail'
            
    def get_sideup(self):
        return self.__sideup
def main():
    # creating object of the class 
    obj1 = Coin()
    # up side of the coin is 
    print("Up side of the coin is : " + str(obj1.get_sideup()))
    
    # tossing of the Coin 
    print("I'm tossing a coin ten times! ")
    for i in range(0,10):
        obj1.toss()
            # After tossing the up side of the coin is 
        print("Up side of the coin is : " + str(obj1.get_sideup()))
    
    
main()