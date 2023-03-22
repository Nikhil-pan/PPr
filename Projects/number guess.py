import random

n= random.randrange(1,10)
print(n)

guess=int(input("Guess a number between 1 and 10:"))

def guess_check(guess,n):
    if(guess == n):
        print(f"Great Guess! You guessed {n} correctly")
    else:
        print("Good Guess! but you are wrong.")
        
def num_check(guess,n):
    if(guess>=1 and guess<=10):
        guess_check(guess,n)
    else:
        print("Invalid Guess!")
        guess=int(input("Try Again:"))
        num_check(guess,n)

num_check(guess,n)