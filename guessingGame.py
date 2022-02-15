import random
print("Number Guessing Game")
number = random.randint(1,9)

chance = 0

while chance < 5:
    guess = int(input("Enter Your Guess:"))
    if guess == number:
        print("Congratulations YOU WIN!!!")
        break
    elif guess < number:
        print("Your guess is low")

    else:
        print("Your guess the high")

    chance += 1

if not chance < 5:
    print("YOU LOSE!! The number is", number)