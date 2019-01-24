lst = input().split()

sumOdd = 0
sumEven = 0

cnt = 1
for num in lst:
	if cnt % 2:
		sumOdd += int(num)
	else:
		sumEven += int(num)
	cnt += 1

print("홀 : %d" %sumOdd)
print("짝 : %d" %sumEven)
