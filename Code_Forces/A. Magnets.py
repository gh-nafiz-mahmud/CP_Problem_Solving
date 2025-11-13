n = int(input())
magnets = [input() for _ in range(n)]
print(1 + sum(magnets[i] != magnets[i-1] for i in range(1, n)))
