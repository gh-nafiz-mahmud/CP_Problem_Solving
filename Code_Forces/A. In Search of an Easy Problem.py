n = int(input())
t = list(map(int, input().split()))
for i in t:
	if i == 1:
		print("HARD")
		break
else:
	print("EASY")