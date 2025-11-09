k,n,w = list(map(int, input().split()))
x = k
sum = 0
for i in range(w):
	x = k * (i+1)
	# print(x)
	sum += x
	# print(sum)
print((sum - n) if (sum - n) > 0 else 0)