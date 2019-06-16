#!/usr/bin/env python

print("Please, enter a word:")
s = input("> ")
r = s[::-1]

if s == r:
    print("It's a palindrome!")
else:
    print("It's NOT a palindrome!")