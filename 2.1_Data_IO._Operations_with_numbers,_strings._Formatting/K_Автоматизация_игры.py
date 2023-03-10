'''Автоматизация игры
Всё в том же детском саду ребята очень любят играть с цифрами.
Одна из таких игр — перестановка цифр четырёхзначного числа.
Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
Формат ввода
Одно четырёхзначное число.
Формат вывода
Одно четырёхзначное число — результат перестановки.
Пример 1
Ввод
1234
Вывод
2143
Пример 2
Ввод
1412
Вывод
4121
Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt
'''
sequence = input()
form = "{1}{0}{3}{2}".format(sequence[:1], sequence[1:2], sequence[2:3], sequence[3:])
print(form)
