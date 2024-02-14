import math
N = int(input())
list = []
list.append(N)
# print(list)
money = 0

while True:
    list = [j for j in list if j != 1]
    # print(list)
    if len(list) == 0:
        break
    money += list[0]
    list.append(math.floor(list[0]/2.0))
    list.append(math.ceil(list[0]/2.0))
    del list[0]
print(money)



        

