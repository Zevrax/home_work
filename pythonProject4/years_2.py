year_in = int(input ("введыть рік для перевірки"))

max = 1000000

min = 1900


if   (year_in >= max or year_in <= min):
    print ("невірний діапазон")


elif ((year_in % 4==0) and (year_in % 100 !=0) or ( year_in % 400==0)):
    print(year_in, "високосний рік")

else: print(year_in, "не високосний рік")
























