# In this version you can choose to play again or stop
import random

print("\nWelcome to Guess The Number!")
print("You have to guess the number that we have in mind.")
print("If you guess wrong we'll help you and tell you if it's too high or too low.")

number = random.randint(0, 100)
guesses = 10
condition = True


def right():
    global condition
    global guesses
    global number
    if Playernumber == number:
        print("YOU GUESSED RIGHT!\n")
        again = input("Do you want to play again? Type Y or N: ")
        if again == 'Y':
            guesses = 10
            print(f"Guesses left: {guesses}")  # Test
            number = random.randint(0, 100)
        elif again == 'N':
            condition = False
        else:
            print("Wrong input")
            condition = False
        print(f"Guesses left: {guesses}")       # Test


def wrong():
    global condition
    global guesses
    if Playernumber > number:
        guesses -= 1
        print(f"You guessed too high.\t Guesses left: {guesses}")
    elif Playernumber < number:
        guesses -= 1
        print(f"You guessed too low.\t Guesses left: {guesses}")


while condition:
    Playernumber = int(input("\nWhat do you guess? "))
    print(f"Guessed number {Playernumber}")             # Test
    print(f"Actual number {number}")                    # Test

    wrong()
    right()

    if guesses <= 0:
        print("\nYou've guessed too many times so you lose!")
        condition = False
