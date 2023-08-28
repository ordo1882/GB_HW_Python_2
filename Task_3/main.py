# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter the number: "))

count = 1

print("Power of 2 numbers line: ")

while count < n:
    count *= 2
    if count > n:
        break
    print(count, end= ' ')