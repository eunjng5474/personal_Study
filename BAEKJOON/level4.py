# # 10807 개수 세기

# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())
# print(n_list.count(v))  # 구글링

# # v_dict = {}
# # for num in n_list:
# #     if num in v_dict:
# #         v_dict[num] += 1
# #     else:
# #         v_dict[num] = 1
# # print(v_dict)

# # v = int(input())
# # if v in v_dict:
# #     print(v_dict[v])
# # else:
# #     print(0)



# # 10871 x보다 작은 수
# n, x = map(int, input().split())
# n_list = list(map(int, input().split()))
# for num in n_list:
#     if num < x:
#         print(num, end = ' ')



# # 10818 최소, 최대
# n = int(input())
# n_list = list(map(int, input().split()))
# print(min(n_list), max(n_list), end = ' ')



# 2562 최댓값
n_list = []
for i in range(9):
    num = int(input())
    n_list.append(num)
# # n_list = enumerate(n_list)
# # print(n_list)
# # print(max(n_list))

# # print(max(n_list))
# # if n_list[id] == max(n_list):
# #     print(id)

# # print(max(n_dic[idx]))
# # if n_dic[idx] == max(n_dic[idx]):
#     # print(idx)


for idx, num in enumerate(n_list):      # 교재 보고 enumerate 사용
    n_max = max(n_list)
    if n_list[idx] == n_max:
        print(n_max)
        print(idx + 1)


# n_max = max(n_list)               # 숏코딩 참고
# idx = n_list.index(n_max) + 1
# print(n_max)
# print(idx)