print("Если захочешь закончить программу напиши ex")
calc = True
while calc:
    calc = input("операцию: +,-,*,/,mod,pow,div:\n")
    if calc == "ex":
        calc = False
        print("Выход из программы")
    if calc in ("+", "-", "*", "/", "mod", "pow", "div" ):
        value_1 = float(input("первое число"))
        value_2 = float(input("второе число"))
        try:
            if calc == "+":
                result = value_1 + value_2
            elif calc == "-":
                result = value_1 - value_2
            elif calc == "*":
                result = value_1 * value_2
            elif calc == "/":
                result = value_1 / value_2
            elif calc == "mod":
                result = value_1 % value_2
            elif calc == "pow":
                result = value_1 ** value_2
            elif calc == "div":
                result = value_1 // value_2
            print(result)
        except ZeroDivisionError:
            print("Деление на 0!")
        except ValueError:
            print("Это не число")
