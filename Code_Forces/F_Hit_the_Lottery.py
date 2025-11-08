n = int(input())

bills = 0

for bill in [100, 20, 10, 5, 1]:
    count = n // bill   # number of bills of this denomination
    bills += count
    n -= count * bill   # remaining amount

print(bills)
