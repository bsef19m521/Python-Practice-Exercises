# In this program , we toss a coin and return head or tail to the user 
import random
class Coin:
    def __init__(self):
        self.sideup = 'Head'
        
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup = 'Head'
        else:
            self.sideup = 'Tail'