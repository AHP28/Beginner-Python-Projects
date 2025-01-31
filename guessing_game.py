import random

def guess(x):
    if x<0:
        guess(int(input("Level: ")))
    rand = random.randint(1, x)
    gues = 0
    tries = 0
    while gues!=rand:
        gues = int(input(f"Guess: "))
        if rand>gues:
            print("Too Small!")
            tries+=1
        elif gues>rand:
            print("Too Large!")
            tries+=1

    print(f"Just right!")

try:
    guess(int(input("Level: ")))
except TypeError:
    guess(int(input("Level: ")))
except ValueError:
    guess(int(input("Level: ")))



