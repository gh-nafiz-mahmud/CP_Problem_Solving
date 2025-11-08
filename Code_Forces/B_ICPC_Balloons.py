t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    first_solved = set()
    total_balloons = 0
    
    for i in s:
        total_balloons += 1
        if i not in first_solved:
            total_balloons += 1
            first_solved.add(i)
    
    print(total_balloons)
