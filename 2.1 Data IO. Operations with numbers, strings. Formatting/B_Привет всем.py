'''Привет, всем!
Но вообще, хорошо бы узнать имя собеседника, а уже потом его приветствовать.

Напишите диалоговую программу, которая сначала познакомится со своим пользователем, а затем поздоровается с ним.

Формат ввода
Одна строка — имя пользователя программы.

Формат вывода:
В первой строке написан вопрос: «Как Вас зовут?» Во второй строке — приветствие пользователя: «Привет, %username%».

Пример 1
Ввод
Ann
Вывод
Как Вас зовут?
Привет, Ann

Пример 2
Ввод
Bob
Вывод
Как Вас зовут?
Привет, Bob

Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt'''

name = input('Как Вас зовут?')
print(f'Привет, {name}')