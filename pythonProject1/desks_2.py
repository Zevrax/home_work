import math
input_1class = int(input("скільки учнів в 1му класі?"))

input_2class = int(input("скільки учнів в 2му класі?"))

input_3class = int(input("скільки учнів в 3му класі?"))

all_students = math.ceil(input_1class/2) + math.ceil(input_2class/2) + math.ceil(input_3class/2)



print("кількість парт що треба закупити",  (all_students),)






























