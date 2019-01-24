def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


cnt = 0
n = 2
while cnt < 100 :
	if isPrime(n):
		print(n, end=' ')
		cnt += 1
	n += 1