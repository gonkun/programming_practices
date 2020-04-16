#!/usr/bin/env python3
# printTable.py - Print a Table with Strings right-justified

tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(table):
    colWidth = []
    for list in table:
        colWidth.append(len(max(list, key=len)))
    print(colWidth)


printTable(tableData)
