i=3
while i!=0:
    print("Meow")
    i=i-1

L=0
while L<=3:
    print("meow")
    L+=1
    
#where range() is an function for looping
for i in range(5):
    print("Meowwwwww")

#where this sign _ is showing the variable we didn't put any word because at that time we don't need it
for _ in range(5):
    print("meowwwwww")

print("meow\n"*3, end="")


#fellow loop is use when we want to match users input according to our reqirenment
while True:
    a=int(input("Enter the value of x"))
    if a>0:
        continue
    else:
        break



#fellow loop is use when we want to match users input according to our reqirenment
#This loop is use while print statement is not run Mean jab tak conditiion true nahi ho jati or Moew run nahi ho jata ya chalti raha gi 
while True:
    n=int(input("How many time you want to say Meow?"))
    if n>0:
        break
for _ in range(n):
    print("meowieoiw")



# In the below program we define a function (get_number) from the user then put that Input in FOR loop to execute as many time as User wants
def main():
    number= get_number()
    meow(number)


def get_number():
    while True:
        z=int(input("Enter the value of z"))
        if z>0:
            break
    return z

def meow(z):
    for _ in range(z):
        print("Meow")

main()


