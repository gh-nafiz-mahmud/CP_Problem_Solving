n = int(input())
s = input()
countD, countA = 0, 0
for i in s:
	if i == 'A':
		countA += 1
	elif i == 'D':
		countD += 1
if countA > countD:
	print("Anton")
elif countA < countD:
	print("Danik")
else:
	print("Friendship")
