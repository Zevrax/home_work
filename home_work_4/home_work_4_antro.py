Num = int(input("введіть число"))

k = 0

for i in range(1, Num + 1):

   k = k + 1

   k_str = str(k)

   k_len = len(k_str)

   i_i = i ** 2

   i_i_str = str(i_i)

   if i_i_str[-k_len:] == k_str:

       print(k_str, '*', k_str, '=', i_i_str)