#!/usr/bin/env python

print("Enter a number for divide: ")
num = int(input("> "))

print("Enter a number for check: ")
check = int(input("> "))


if num % 2 == 0:
    if num % 4 == 0:
        print(str(num) + " is a even number and multiple of 4")
    else:
        print(str(num) + " is a even number")
else:
    print(str(num) + " is a odd number")


if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
