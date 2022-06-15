import random

# list of all the puncutation signs 
punctutaionSigns = ['!','@','#','$','%','^','&','*','(',')']
# two random generated upper case letters
upperCaseLetters = chr(random.randint(65,90)) + chr(random.randint(60,90))
# two random generated lower case letters
lowerCaseLetters = chr(random.randint(97,122)) + chr(random.randint(97,122))
# two random generated integer numbers
# str function is used convert integer generated numbers into a string
digits = str(random.randint(0,9)) + str(random.randint(0,9))
# two random generated puncutation characters
specialCharacters = random.choice(punctutaionSigns) + random.choice(punctutaionSigns)
password = list(upperCaseLetters+lowerCaseLetters+digits+specialCharacters)
# shuffle method shuffled all the elements of the list and return None 
random.shuffle(password)
shuffledPassword = "".join(password)
print(f"Your 8 character random generated password is :  {shuffledPassword}")