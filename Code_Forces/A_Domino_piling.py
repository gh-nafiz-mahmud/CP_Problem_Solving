m, n = map(int, input().split())

if ((m * n) % 2) == 0:
    print(f"{int((m * n) / 2)}")
else:
    print(f"{int(((m * n) - 1) / 2)}")
