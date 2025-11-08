t = int(input())
for i in range(t):
	a,b,c = map(int, input().split())
	sortedList = sorted([a,b,c])
	if sortedList[2] == (sortedList[0]+sortedList[1]):
		print("YES")
	else:
		print("NO")
