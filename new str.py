value = int(input("Введите число :"))
new_value = value/2 if value < 100 else - value
print(int(new_value))
####################################################################
value_1 = int(input("Введите число:"))
new_value_1 = 1 if value_1 < 100 else 0
print(new_value_1)
#################################################################
value_2 = value < 100
print(value_2)
# ###################################################################
my_str = "qwerty"
my_str_2 = my_str * 2 if len(my_str) < 5 else my_str
print(my_str_2)
########################################################
my_str = "qwer"
my_str_2 = my_str[::-1] if len(my_str) < 5 else my_str
print(my_str_2)