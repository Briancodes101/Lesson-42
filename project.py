import random 

def number():
    guess = random.randint(1, 20)
    
    print("Guess a number (between 1 and 20):")
    
    while True:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < guess:
                print("Too low, The number is", guess)
            elif user_guess > guess:
                print("Too high, The number is", guess)
            else:
                print("Congratulations! You guessed the number")

number()