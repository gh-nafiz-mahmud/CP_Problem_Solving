n,t= list(map(int, input().split()))
s = input()

for i in range(t):
	x=0
	y=2
	list_s = list(s)
	while y <= n:
		if s[x:y] == "BG":
			list_s[x], list_s[x+1] = "G", "B"
		x+=1
		y+=1
	s = "".join(list_s)

print(s)

