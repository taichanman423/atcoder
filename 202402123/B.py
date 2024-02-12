# n = int(input())
# n_list = []
# for i in range(n):
#     n_list.append(list(map(int,input().split())))
# print(n_list)

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
# print(n_list)

num_list = []
for i in range(n):
    if n_list[i][0] == 1:
        num_list.append(n_list[i][1])
        # print(num_list)
    else:
        print(num_list[len(num_list)-n_list[i][1]])