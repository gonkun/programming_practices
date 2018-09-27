a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b =[]

for num in a:
    if num < 5:
        b.append(num)
        print(num)

print(b)

c = []
num2 = int(input("Please, enter a number:> "))

for num in a:
    if num < num2:
        c.append(num)

print(c)