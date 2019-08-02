def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return (3 * number + 1)

print('Enter number:')
try:
    num = int(input())
except ValueError:
    print('Invalid Argument.')
    exit(1)

while num != 1 and num != 0:
    num = collatz(num)
    print(num)