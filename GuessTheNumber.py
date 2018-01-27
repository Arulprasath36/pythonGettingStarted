import random

number_on_mind=random.randint(1,20)
print("I thought of a number between 1 to 20. Guess it")

for guesses in range(1,7):
    print('Guess the number')
    user_said=int(raw_input())

    if(user_said<number_on_mind):
        print("Your answer is lower than I thought")
    elif user_said>number_on_mind:
        print("Your answer is lower than I thought")
    else:
        break

if user_said==number_on_mind:
    print("Great! You found my number on"+ str(guesses)+" attempts")
else:
     print("Nope! The number I was thniking was " + str(number_on_mind))