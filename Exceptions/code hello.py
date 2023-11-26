#Exceptopn means something wronge or missing
#Syntax Error: is a problem with the code that we have typed
#Runtime Error: The Error come while running the Code 
#Value Error: 
#below is an exmple how to handle Value Error
try:
    x=int(input("what's the x"))
except ValueError :
    print("x is not an integer")
else:
    print("sadfhgfgsajf")


def main():
    x=get_int()
    print(f"x is equal to {x} ")
# define my own function called get_int()
def get_int():
#where loop which while the condition will to true
    while True:
        try:
            x=int(input("what's the x"))
        except ValueError :
            print("x is not an integer")
        else:
            break
    return x

main()
#we can also doing upper code as below 

def main():
    x=get_int("WHat's the value of x")
    print(f"x is equal to {x} ")
# define my own function called get_int()
def get_int(Prompt):
#where executed untill while loop the condition will be true
    while True:
        try:
            return int(input(Prompt))
        except ValueError :
#we can also handle by using pass function
            pass


main()
# NAme Error: This type of error occur when something is not define but is used 

try:
    x=int(input("what's the x"))
except ValueError :
    print("x is not an integer")
else:
    print(f"x is {x}")