sum = int(input("сума кредиту"))

pr_1 = sum / 100

pl_2 = sum / 60 + pr_1 * 2

pl_4 = sum / 60 + pr_1 * 4

pl_1_2 = sum / 12 + pr_1 * 2

spasce = '10.2f'
# spasce_2 = 40
m = 00

while m < 60:
    m += 1

    if m < 13:

        print(f"{m:02}, {pl_2:{spasce}},  | {pl_1_2:{spasce}},  | {pr_1*2:{spasce}}")

    elif m > 13:

        print(f"{m}, {pl_2:{spasce}},  | {pr_1*4:{spasce}}")