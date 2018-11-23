temp = input()
numlist = temp.split(' ')
n = len(numlist)
result = 0
 
for i in range(n, 0, -1):
    from itertools import combinations
    newlist = list(combinations(numlist, i))
    break_statement = 0
    for item in newlist:
        isup = 1 
        for j in range(i-1):
            if item[j]>=item[j+1]:
                isup = 0
                break
        if isup == 1:
            result = i
            break_statement = 1
            break
    if break_statement:
        break

print(result)
