def main():
    n=int(input("what's x?"))
    if is_even(n):
        print("Even")
    else:
        print("Odd")
        
#[def is_even(n):
#    if n%2==0:
#        return True
#    else:
#        return False]
    
#{def is_even(n):
#    return True if n%2==0 else False}
#main()

def is_even(n):
    return(n%2==0)
main()