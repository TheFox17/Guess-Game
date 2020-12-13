import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print('Too low. Try again!')
        elif guess > random_number:
            print('Too high. Try again!')  
    print(f"Congratzzz!. You guessed the number ({random_number}) correctly!") 

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ' ).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Haha, I've guess the number {guess} and won bitch! Let's do it again!")


choice = int(input("Welcome to Talson's Joy Land!\nYou gotta choose, do you want to guess the number(1)? or make the computer guess(2)?\n> "))
if choice == 1:
    users_num = int(input("Okay,now you are going to guess the number. What's the range you want? 10, 100, or 1000!\n> "))
    guess(users_num)
elif choice == 2:
    users_num = int(input("Okay, now the computer is going to guess the number. What's the range you want? 10, 100, or 1000!\n> "))
    computer_guess(users_num)
else:
    choice = int(input("Please input a number. Either 1 or 2: "))
