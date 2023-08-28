# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

coins = int(input("Enter the number of coins: "))

head = 0
tail = 0

for i in range(coins):
    value = random.randint(0, 1)
    print(value, end= ' ')
    if value == 1:
        head += 1
    else:
        tail += 1

print(f"\nNeed to flip {head} coins") if head < tail else print(f"Need to flip {tail} coins")