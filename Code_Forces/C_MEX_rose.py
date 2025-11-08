# def mex_a(a):
#     b = set(a)
#     i = 0
#     while True:
#         if i not in b:
#             return i

# t = int(input())
# for i in range(t):
#     n, k = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     x = mex_a(a)
#     if x == k:
#         print(0)
#     elif x < k:
#         print(1)
#     else:
#         print(a.count(k))
