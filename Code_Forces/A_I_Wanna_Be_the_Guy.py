n = int(input())
p_levels = list(map(int, input().split()))
q_levels = list(map(int, input().split()))

all_levels = set(p_levels[:] + q_levels[:])

if len(all_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
