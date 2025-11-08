t = int(input())
n = list(map(int, input().split()))

parity = [n[0] % 2, n[1] % 2, n[2] % 2] # list of odd or even
majority_even = parity.count(0) > 1  # True if not odd

for i in range(len(n)):
    if (n[i] % 2 == 0) != majority_even:
        print(i + 1)
        break