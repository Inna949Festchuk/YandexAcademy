'''Деловая колбаса
Настало время для действительно серьёзных задач...
В детском саду 2 ребенка съедают 2 куска колбасы за 2 минуты. Сколько кусков колбасы за �N минут съедят �M детей?
Формат ввода
В первой строке записано натуральное число N≥1
Во второй строке записано натуральное число M≥1
Формат вывода
Одно натуральное число — количество кусков колбасы, съеденных детьми
Примечание
Гарантируется, что в результате вычислений будет получено натуральное число.
Пример 1
Ввод
2
2
Вывод
2
Пример 2
Ввод
10
10
Вывод
50
Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt
'''
child = int(input())
sausage = int(input())
print((child * sausage) // 2)
