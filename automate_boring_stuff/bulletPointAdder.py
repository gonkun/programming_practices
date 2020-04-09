#!/usr/bin/env python3
# bullentPointAdder.py - Adds Wikipedia bullet points to start
# of each line of textin the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
  lines[i] = '* ' + lines[i]    # add start to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)