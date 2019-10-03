# important imports
import random
from itertools import product

# Where are we heading?
desire = input("do you want random numbers(y/n): ")

if desire == "y":

    iterations = int(input("how many do you need: "))
    lower = int(input("lowest number? "))
    upper = int(input("highest number? "))
    dice = int(input("How many dice do you want? "))
    x = 0

    while x < iterations:
        total = 0
        z = 0
        while z < dice:
            num1 = random.randint(lower, upper)
            total = total+num1
            z = z+1
        print(total)
        x = x + 1
else:
    freq = input("do you want frequencies(y/n)? ")

if freq == "y":
    dice_value = input("what are all the dice values: ")
    reepeat = int(input("what repeat value you want? "))

    print(list(product(dice_value, repeat=reepeat)))

else:
    print("bye felicia")
