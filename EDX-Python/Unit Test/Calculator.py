#unit testing is just a formal way of describing testing indivitual unit of our program
#Unit test are typically tests for function that we are written




def main():
    x=input("What's x?")
    print("x suqare is ", square(x))



def square(n):
    return n*n

if __name__=="__main__":
    main()