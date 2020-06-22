#third program

a= int(input("enter the first value:"))

b= int(input("enter the second value:"))

c= a + b

print("the sum of {0} and {1} is {2}".format(a, b, c))

if c > 5:
    print(" the sum is  grater than 5")

elif c < 5: 
    print("the sum isless than 5")

else:
    print("the sum is  equal to 5")