#program to find max of three numbers 

a= int(input("enter the first digit:"))

b= int(input("enter the second digit:"))

c= int(input("enter the third digit:"))

if (a>=b) and (a>c):
    print("first digit is greater")

elif(b>=a) and (b>=c):
    print("second digit is greater")

else:
    print("third digit is greater")
