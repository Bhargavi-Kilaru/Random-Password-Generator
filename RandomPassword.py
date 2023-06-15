import random
import string

print("The Random Password Generator")
print("Select the type of Password:")
print("1.Aplhabets Password:")
print("2.Aplha_Numeric Password:")
print("3.Numeric Password:")
print("4.Alphabets and Special Charcaters Password:")
print("5.Numbers and Special Characters Password:")
print("6.Strong Password:")


def alpha(n):
    password=""
    req=string.ascii_letters
    for i in range(n):
        password+=(random.choice(req))
    print("The Alphabetical password with size ",n,"  is: ",password)
def aplha_numeric(n):
    password=""
    req=string.ascii_letters+string.digits
    for i in range(n):
        password+=(random.choice(req))
    print("The Alpha Numerical password with size ",n," is: ",password)
def numeric(n):
    password=""
    req=string.digits
    for i in range(n):
        password+=(random.choice(req))
    print("The Numerical password with size ",n,"  is: ",password)
def alpha_special(n):
    password=""
    req=string.ascii_letters+string.punctuation
    for i in range(n):
        password+=(random.choice(req))
    print("The Aphabets and Special Charctered Password with size ",n," is:",password)
def numeric_special(n):
    password=""
    req=string.digits + string.punctuation
    for i in range(n):
        password+=(random.choice(req))
    print("The Numerical password with size ",n,"  is: ",password)
def strong(n):
    password=""
    req=string.ascii_letters + string.digits + string.punctuation
    for i in range(n):
        password+=(random.choice(req))
    print("The Strong password with size ",n," is: ",password)

#The switch case for the choice for the user       
while(1):
    select=int(input("Enter your choice:"))
    if(select==1):
        n=int(input("Enter the number of Alphabetical password:"))
        alpha(n)
    elif(select==2):
        n=int(input("Enter the number of alpha_numeric password:"))
        alpha_numeric(n)
    elif(select==3):
        n=int(input("Enter the number of Numerical password:"))
        numeric(n)
    elif(select==4):
        n=int(input("Enter the number of aplhabets and special password:"))
        alpha_special(n)
    elif(select==5):
        n=int(input("Enter the number of Numerics and Special password:"))
        numeric_special(n)
    elif(select==6):
        n=int(input("Enter the number of strong password:"))
        strong(n)
    else:
        print("Thank You for using our Random Password Generator")
        break
