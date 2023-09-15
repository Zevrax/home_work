def has_sum_equal_to_target(numbers, target):
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False


user_input = input("Введіть числа через пробіл: ")
numbers = [int(x) for x in user_input.split()]


target = int(input("Введіть цільове число: "))


result = has_sum_equal_to_target(numbers, target)
if result:
    print(f"У списку є два числа, сума яких дорівнює {target}.")
else:
    print(f"У списку немає двох чисел, сума яких дорівнює {target}.")