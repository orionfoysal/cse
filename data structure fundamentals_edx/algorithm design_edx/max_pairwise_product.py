#python3

n = int(input())
num = [int(x) for x in input().split()]

# product = 0
# for j,i in enumerate(num):
#     # print(j)
#     for k in num[j+1:]:
#         product = max(product, i*k)
# print(product)

# sort first

num.sort()
print(num[-1]*num[-2])