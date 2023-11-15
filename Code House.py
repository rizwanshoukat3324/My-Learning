name=input("Enter your State name?")
if name=="Punjab" or name == "Karachi" or name=="Lahore":
    print("You are pakistani and you live in ",name)
else :
    print("you are Not pakistani")
    

#Switch Staetment
Name=input("Enter your's Name?")
match Name:
    case "Rizwan" | "Shoukat" | "Imran":
        print(Name,"You are most welcome to Trendsminder! ")
    case "Shaban" | "Ramzan" | "Ali Shan":
        print(Name,"This is not your Office!")
    case _:
        print("You are not Recognize Person Show your Identity")
        
#in Third case "_" this symbol is used for else.