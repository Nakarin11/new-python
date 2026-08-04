#This program simulates 10 tosses of a coin.
import random

#Contants
HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")

#Call the function
tosses_coin()