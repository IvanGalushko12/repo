# Списки:

i_am = []
i_am.append("Ivan")
print(id(i_am))
i_am.append("Galushko")
print(i_am, id(i_am))

print("-----------------")

# Срезы:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[0:5])
print(numbers[-6:])
print(numbers[1::2])

# Вложенные списки:

print("-----------------")

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nested_list[1][0] = 42

print(nested_list)

temp = nested_list[0][2]
nested_list[0][2] = nested_list[1][1]
nested_list[1][1] = temp

print(nested_list)