# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

from math import sqrt

sum = int(input("Enter the sum of numbers: "))
mult = int(input("Enter the multiplication of numbers: "))

D = sum * sum - 4 * mult  # Считаем дискриминант
sq = sqrt(D) / 2
p = sum / 2
num1 = round(p - sq)
num2 = round(p + sq)

print(f"\nNumbers are: {num1} and {num2}\n")