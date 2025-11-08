matrix = list()
for i in range(5):
	row = list(map(int, input().split()))
	matrix.append(row)
for i in range(5):
	if 1 in matrix[i]:
		print(abs((i + 1) - 3) + abs((matrix[i].index(1) + 1) - 3))
		break


# for i in range(5):
# 	for j in range(5):
# 		print(matrix[i][j], end=" ")
# 	print()
