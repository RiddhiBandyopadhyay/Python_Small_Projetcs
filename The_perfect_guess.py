import random
import time

print("Welcome to 'The Perfect Guess' game\n")
ch = ""
while(ch != 'Q'):

    t = int(input("Enter how many rounds you want to play : "))
    comp_ch = random.randint(1, 10)
    comp_score = 0
    pl_score = 0
    name = input("Enter your name : ")
    print("Computer is generating a number...\n")
    time.sleep(1)
    print("Okay, now it's your turn to guess the number -------")

    while(t):
        n = int(input("Guess a number between 1 and 10 : "))
        if n == comp_ch:
            print("Yes, you guessed it right!")
            pl_score = pl_score + 1
            break
        elif n < comp_ch:
            print(f"The number is larger than {n}")
            comp_score = comp_score + 1
        elif n > comp_ch:
            print(f"The number is smaller than {n}")
            comp_score = comp_score + 1
        t = t-1

    if pl_score == 0:
        print(f"Sorry you lost the game, computer's choice was {comp_ch} and your last choice was {n}")
    else:
        print(f"Hurray you won,your score is {pl_score}")

    ch1 = input("Do you want to play again? Press 'C' to continue and 'Q' to quite : ")
    ch = ch1.capitalize()

