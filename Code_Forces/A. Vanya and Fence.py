n,h = list(map(int, input().split()))
a = list(map(int, input().split()))

count_less = 0
count_high = 0
for i in range(0, len(a)):
	if a[i] <= h:
		count_less += 1
	elif a[i] > h:
		count_high += 2
print(count_less + count_high)