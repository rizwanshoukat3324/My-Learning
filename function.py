def gmean(a, b):
    mean=(a*b)/(a+b)
    print(mean)


a=int(input("Enter your value of a"))
b=int(input("Enter your value of b"))
print(gmean(a, b))


#a = int(a)  # Convert 'a' to an integer
#b = int(b)  # Convert 'b' to an integer
#mean = (a * b) / (a + b)


def isgreater(a, b):
    if(a>b):
        print("your first number is greater")
    else:
        print("your second number is graeter")

a=int(input("Enter your value of a"))
b=int(input("Enter your value of b"))
print(isgreater(a, b))