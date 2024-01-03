#!/usr/bin/python3
import random
number = random.randiant(-5, 5)
if number > 0:
    print("{:d} is positive".format(number))
elif number < 0:
    print("{:d} is negative".format(number))
else:
    print("{:d} is zero".format(number))
