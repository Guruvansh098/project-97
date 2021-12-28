import random
number=random.randint(1,9)
chances=0
print("ENter A Number Between 1 And 9")
while chances <3:
    guess=int(input("Enter Your Guess"))
    if guess==number:
        print("You Win")
        break
    elif guess >number:
        print("Please Guess A Smaller Number")
    else:
        print("Please Enter A Bigger Number")
    chances=chances+1
if not chances <3:
    print("You Lose the no was",number)