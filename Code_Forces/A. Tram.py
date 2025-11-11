n = int(input())
exist = 0
main_list = list()
for i in range(n):
	a,b = list(map(int, input().split()))
	exist = exist - a + b
	main_list.append(exist)

print(max(main_list))
