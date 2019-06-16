#!/usr/bin/env python

import datetime

print("Enter your name: ")
name = input("> ")

print("Enter your age: ")
age = int(input("> "))
born_year = int(datetime.date.today().year) - age

print("How many time do you want toprint the same message? ")
times = int(input("> "))

print(times * f"Your name is {name} and you will be 100 years on {born_year + 100}\n")
