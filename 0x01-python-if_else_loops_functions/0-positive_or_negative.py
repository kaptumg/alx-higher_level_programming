#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(number)
if number > 0:
     print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
