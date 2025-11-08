t = int(input())
for i in range(t): 
    total = 0
    n = int(input())
    m = list(map(int, input().split()))
    smaller = min(m)
    for i in m: 
        total += (i - smaller)
    print(total)
