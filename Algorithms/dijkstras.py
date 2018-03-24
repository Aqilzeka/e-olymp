def Dijkstra(N, S, matrix):
	valid = [True]*N
	weight = [1000000]*N
	weight[S] = 0
	for i in range(N):
		min_weight = 1000001
		ID_min_weight = -1
		for i in range(len(weight)):
			if valid[i] and weight[i] < min_weight:
				min_weight = weight[i]
				ID_min_weight = i
		for i in range(N):
			if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
				weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
		print(valid)
		valid[ID_min_weight] = False
	return weight

inf = float("inf")
matrix = [[inf,2,inf,1,inf],
		[2,inf,inf,inf,5],
		[inf,inf,inf,5,1],
		[1,inf,5,inf,inf],
		[inf,6,1,inf,inf]]
print(matrix)

print(Dijkstra(5,0,matrix))
