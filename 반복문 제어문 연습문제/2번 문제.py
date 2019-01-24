a = int(input())

result = 0

if a > 0:
	num = a
	while num <= 3*a:
		result += num
		num += 1

else:
	num = 3*a
	while num <= a:
		result += num
		num += 1

print(result)