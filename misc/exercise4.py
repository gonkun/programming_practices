print("Enter a number:")
num = int(input("> "))

list_range = list(range(1, num + 1))

divList = []
for n in list_range:
    if num % n == 0:
        divList.append(n)

print(divList)