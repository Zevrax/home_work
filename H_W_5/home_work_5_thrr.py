number = int(input("введіть число"))

v1 = "1"
v2 = "0"
v3 = ""
for i in range(number):
    if i > 9:
        print(i, v1.rjust(number + 2 - i) + v2 * i)
    if i < 10:

        print(v3, i, v1.rjust(number+2-i) + v2 * i)










