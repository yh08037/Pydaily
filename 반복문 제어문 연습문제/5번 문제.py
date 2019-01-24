import math

def findRoot(a, b, c):
	if a == 0:
		return - c/b
	
	D = b*b - 4*a*c

	if D < 0:
		return None

	elif D == 0:
		return -b/(2*a)

	else:
		return (-b-math.sqrt(D))/(2*a), (-b+math.sqrt(D))/(2*a)


a, b, c = input().split()

print(findRoot(int(a), int(b), int(c)))