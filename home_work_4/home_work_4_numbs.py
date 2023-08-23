num_list = []




while True:
    num = int(input("wwww"))

    if num == 0:
        break
    else:
        num_list.append(num)

sum_numbers = sum(num_list)

max_num = max(num_list)

mid_a = sum_numbers // len(num_list)

min_num = min(num_list)

e_nums = sum(map(lambda n: not n % 2, num_list))
o_nums = sum(map(lambda n: n % 2, num_list))


print('Количество четных: ', e_nums)
print('Количество нечетных: ', o_nums)
print("midl", mid_a)
print("sum", sum_numbers)
print("max num", max_num)
print("min num", min_num)