a = int(input())

result = 0

min, max = a, 3*a
if a < 0:
	min, max = max, min

num = min
while num <= max:
	result += num
	num += 1

print(result)