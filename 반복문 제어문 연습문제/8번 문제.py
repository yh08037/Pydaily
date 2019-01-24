score = []

for i in range(int(input("학생 수 : "))):
	temp = []
	for j in range(3):
		temp.append(int(input()))
	score.append(temp)
	print()


# 개인별 총점

personalTotal = []
cnt = 1
for lst in score:
	sum = 0
	for num in lst:
		sum += num
	print("학생%d의 총점 : %d" %(cnt, sum))
	personalTotal.append(sum)
	cnt += 1

print()


# 개인별 평균
cnt = 1
for num in personalTotal:
	print("학생%d의 평균 : %.2f" %(cnt, num/3))

print()

# 과목별 총점

subjectTotal = []
cnt = 1
for i in range(3):
	sum = 0
	for num in score:
		sum += num[i]
	print("과목%d의 총점 : %d" %(cnt, sum))
	subjectTotal.append(sum)
	cnt += 1

print()

# 과목별 평균
cnt = 1
for num in subjectTotal:
	print("과목%d의 평균 : %.2f" %(cnt, num/3))
	cnt += 1

