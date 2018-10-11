def transform(data):
	n = len(data)

	original_suffixes = []
	for _ in range(0, n):
		original_suffixes.append(data)
		data = data[1:] + data[0]

	sorted_suffixes = original_suffixes[:]

	sorted_suffixes.sort()

	first = -1

	for _ in range(0, n):
		if (data == sorted_suffixes[_]):
			first = _

	data = ""

	for sorted_string in sorted_suffixes:
		data += sorted_string[-1:]

	print("transformed:", data)
	return [data, first]

def inverseTransform(data, first):
	n = len(data)

	sorted_data = ''.join(sorted(data))

	visited = [False] * n
	next_index = [-1] * n

	for i in range(0, len(sorted_data)):
		for j in range(0, len(data)):
			if (sorted_data[i] == data[j] and visited[j] != True):
				next_index[i] = j
				visited[j] = True
				break

	data = ""
	idx = first
	visited = [False] * n

	while visited[idx] != True:
		data += sorted_data[idx]
		visited[idx] = True
		idx = next_index[idx]

	print("inverse transformed:", data)

	return data







