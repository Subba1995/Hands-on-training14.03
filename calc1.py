print("Введите желаемое действие")
calc = input("+,-,*,/ :")
if calc not in ('+', '-', '*', '/'):
    print('конец программмы')
    quit()
num_1 = input("Введите первое число")
try:
    num_1 = float(num_1)
except ValueError:
    num_1 = input("Та введи ты число, тебе что не интересно")
    try:
        num_1 = float(num_1)
    except ValueError:
        print("Остановись пока не позно!!")
num_2 = input("Введите второе число")
try:
    num_2 = float(num_2)
except ValueError:
    num_2 = input("Ну я же попоросил написать число:")
    try:
        num_2 = float(num_2)
    except ValueError:
        print('Это была последняя капля')

if calc == '+':
    print(num_1 + num_2)
elif calc == '-':
    try:
        print(num_1 - num_2)
    except TypeError:
        print("Я смотрю ты всё таки стараешься")

elif calc == '*':
    print(num_1 * num_2)
elif num_2 != '0':
    print("На ноль делить нельзя")
else:
    print(num_1 / num_2)
