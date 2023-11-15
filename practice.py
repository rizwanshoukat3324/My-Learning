# Conditional Tests
# 5-1
car = "mehran"
print("Is car== Mehran? I predict true ")
print(car == 'mehran')

# 5-2
Fruit = 'Grapes'
print(" Is Fruit == 'Grapes'? I predict True")
print(Fruit == 'Grapes')

# 5-3
Car = 'Ferrari'
print(" Is Car == 'Picanto'? I predict True")
print(Car == 'Range Rover')


# If Condition
# 5-1
alien_colur = input("Enter Alien colur so that we start game?")
if alien_colur == "Green" or "yellow" or "red":
    print("Your earned 5 points")


# 5-2
Person = input("Enter your Company, where you doing Job? ")
if Person == "Army" and "Navy" or "Air Force":
    print("You are serving country as many Yougster want! Great Job")


# 5-3
Car = input('Enter your car Name?')
if Car == "Audi" and "Suzuki" and "Mehran" and "Rang Rovers" and "Ferrari":
    print("You have amazing collection of cars!")


# If else Statement
# 5-1
Person = input("Enter your Company, where you doing Job? ")
if Person == "Army" or "Navy" or "Air Force":
    print("You are serving country as many Yougster want! Great Job")
else:
    print("You are not a Militry Person!")

# 5-2
Age = int(input("Enter You age?"))
if Age <= 18:
    print("you are not Able to Vote!")
else:
    print("you are able to Vote")


#5-3
Car = input('Enter your car Name?')
if Car == "Audi" and "Suzuki" and "Mehran" and "Rang Rovers" and "Ferrari":
    print("You have amazing collection of cars!")
else:
    print("your car collection is not Good!")
    

#IF Elif else Chain
#5-1
alien_colur = input("Enter Alien colur so that we start game?")
if alien_colur == "Green" :
    print("Your earned 5 points")
elif alien_colur== 'Black':
    print('You earned 10 points')
elif alien_colur=='red':
    print(' your earned 15 points')
else:
    print("Your are failed in the Game")


#5-2
Person_Age=int(input("Enter Your Age?"))
if Person_Age<=2:
    print('Your are baby!')
elif Person_Age>=2 and Person_Age<=4:
    print('You are Toddler')
elif Person_Age>=4 and Person_Age<=13:
    print('you are kid')
elif Person_Age>=13 and Person_Age<=20:
    print('you are younger')
else:
    print('you are elder')
    
#5-3

Favorite_food=['Banana','Grapes','Mango','Apple']
x=input('Enter you Favorite Fruit Name?')
if x==Favorite_food:
    print(" you have really Good Choice!")