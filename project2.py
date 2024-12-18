# Its a Perfect Guess Game
import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess a Number: "))
    if(a>n):
        print("Lower Number please..")
        guesses+=1
    elif(a<n):
        print("Higher number Please..")
        guesses+=1

print(f"Yeah!! You have guessed the Number {n} in {guesses} attempts.")