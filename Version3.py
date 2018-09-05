# In this version you can choose to play again to win more money or stop and keep the money
import random

print("\nWelcome to Guess The Number!")
print("You have to guess the number that we have in mind.")
print("If you guess wrong we'll help you and tell you if it's too high or too low.")
print("If you guess right you may choose to stop and keep the money or to play again to win $5 more.")

number = random.randint(0, 100)
guesses = 10
condition = True
money = 0


def right():
    global condition
    global guesses
    global number
    global money
    if Playernumber == number:
        money += 5
        print(f"\nYOU GUESSED RIGHT!\nYou've won $5!\t Money: ${money}")
        again = input("\nDo you want to play again? Type Y or N: ")
        if again == 'Y':
            guesses = 10
            number = random.randint(0, 100)
        elif again == 'N':
            condition = False
            print(f"You've won ${money}!")
        else:
            print("Wrong input")
            condition = False


def wrong():
    global condition
    global guesses
    global money
    if Playernumber > number:
        guesses -= 1
        print(f"You guessed too high.\t Guesses left: {guesses}\tMoney: ${money}")
    elif Playernumber < number:
        guesses -= 1
        print(f"You guessed too low.\t Guesses left: {guesses}\tMoney: ${money}")


while condition:
    Playernumber = int(input("\nWhat do you guess? "))

    wrong()
    right()

    if guesses <= 0:
        print("\nYou've guessed too many times so you lose!")
        condition = False
