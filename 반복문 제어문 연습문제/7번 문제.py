def summation(n):
	result = 0
	for i in range(n):
		temp = 0
		for j in range(1, i+2):
			temp += j
		result += temp
	return result

print(summation(int(input())))
