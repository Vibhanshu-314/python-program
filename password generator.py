import random
import string



def generrate_password():
    print("------password generator-----")
    
    
    length=int(input("Enter the password lentgth:"))
    
    
    
    ## kaunse kaunse character aa skte haii
    # digits ayenge #alphabets # symbols bhi aa skate hai
    
    letters=string.ascii_letters
    digits=string.digits
    symbol=string.punctuation
    
    all_chars=letters+digits+symbol
    
    
    # generate password 
    password=[]
    for i in range (length):
        char=random.choice(all_chars)
        
        password.append(char)
        
    password="".join(password)    
    print("genrates password :",password)
 # call bhi toh krna pdega    
generrate_password()    