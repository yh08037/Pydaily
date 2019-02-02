'''
print("  *  ")
print(" *** ")
print("*****")
'''
'''
num=int(input("열의 개수 : "))
num2 = int(input())
for i in range(num):
	print((" "*(num-1-i)+"*"*(i*2+1)+" "*(num-1-i))*num2)
'''

for student in [1,2,3,4,5]:
	print("%d%d번 학생" %(student,student))