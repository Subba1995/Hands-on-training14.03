# 1.
my_int = 4004003020320
result = str(my_int)
print(result.count('0'))
# 2.
number = 1002000
my_str = str(number)
result = len(my_str) - len(my_str.rstrip('0'))
print(result)
# 3.
my_list_1 = ["qwerty","value","somthing","hello"]
my_list_2 = ["1111","buy","test","book"]
result = my_list_1[::2] + my_list_2[1::2]
print(result)
# 4.
my_list = [1, 2, 3, 4]
new_list = my_list[1:] + [my_list[0]]
print(f"{new_list=}")
# 5.
my_list = [1, 2, 3, 4]
list_value = my_list.pop(0)
my_list.append(list_value)
print(my_list)
# 6.
my_string = "43 больше чем 34 но меньше чем 56"
my_str_list = my_string.split()
counter = 0

for item in my_str_list:
    if item.isdigit():
        counter += int(item)

print(counter)
# 7.
my_str = "My long string"
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]
sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
print(sub_str)
# 8.
example = 'abcde'

result_list = []
example_ = len(example)
for index in range(0, example_, 2):
    if index < example_ - 1:
        result_list.append(example[index] + example[index + 1])
    else:
        result_list.append(example[index] + '_')
print(result_list)
# 9.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
print(sum(my_list))
counter = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
        counter += 1
# 10.
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for symbol in my_list:
    if my_list != int:
        new_list.append(symbol)
print(new_list)