my_list = [34, 75, 103, 643, 89]
for value in my_list:
    if value > 100:
        print(value)

#####################################
my_list = [34, 75, 103, 643, 89]
my_result = []
for value in my_list:
    if value > 100:
        my_result.append(value)

print(my_result)

#####################################
my_list = [34, 75, 103, 643, 89]
if len(my_list) < 2:
    my_list.append(0)
else:
    sum = my_list[-1] + my_list[-2]
    my_list.append(sum)
print(my_list)