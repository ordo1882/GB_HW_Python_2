# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Enter the number: "))

count = 1
condition = True

print("Power of 2 numbers line: ")

while condition:
    count *= 2
    
    if count > n:
        condition = False
    else:
        print(count, end= ' ')