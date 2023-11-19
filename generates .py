import random

coin=random.choice(["heads", "tails"])
print(coin)

number=random.randint(1,76)
print(number)

cards=["Rizwan","Imran","Shaban","Alishan","Ramzan"]
random.shuffle(cards)
for card in cards:
    print(card)