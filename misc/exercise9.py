#!/usr/bin/env python
__author__ = 'gonzalo.sanchter@gmail.com'

import random

def compare(a, b):
    

n = random.randint(1,9)

num_tries = 0
quie = False

print("A random integernumber has been generated...")

while (quit != False ):
    print("Please, enter a integer and try to guess the mysterious number:")
    x = input("> ")
    if x == "exit":
        break
    
    num_tries = num_tries + 1

    if int(x) == n:
        print("Congratulations! You did it!")
        break
    elif int(x) > n:
        print("Your number is too high")
    elif int(x) < n:
        print("Your numver is too low")

print("Mysterious number: ", n)
print("Number of tries: ", num_tries)