import random

# list of all the punctutaion signs 
punctutaionSigns = ['!','@','#','$','%','^','&','*','(',')']
# two random upper case letters
upperCaseLetters = chr(random.randint(65,90)) + chr(random.randint(60,90))
lowerCaseLetters = chr(random.randint(97,122)) + chr(random.randint(97,122))
digits = str(random.randint(0,9)) + str(random.randint(0,9))
specialCharacters = random.choice(punctutaionSigns) + random.choice(punctutaionSigns)
password = list(upperCaseLetters+lowerCaseLetters+digits+specialCharacters)
random.shuffle(password)
shuffledPassword = "".join(password)
print(f"Your 8 character random generated password is :  {shuffledPassword}")