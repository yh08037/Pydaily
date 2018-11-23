n = int(input())
name = []
score = []
result = []

for a in range(n):
    temp = input()
    temp = temp.split(' ')
    name.append(temp[0])
    score.append(temp[1])
    result.append(temp[0])

newname = []
newscore = []
loopcnt = []
loopcnt.append(n)

while True:
    newname = []
    newscore = []
    isodd = len(name)%2
    num = int(len(name)/2)
    for i in range(num):
        if int(score[2*i])>int(score[2*i+1]):
            newname.append(name[2*i])
            newscore.append(score[2*i])
        else:
            newname.append(name[2*i+1])
            newscore.append(score[2*i+1])
    if isodd:
        newname.append(name[-1])
        newscore.append(score[-1])
    result = newname + result
    loopcnt.insert(0, len(newname))
    name, score = newname, newscore
    if len(newname)==1:
        break


cnt = 0

for item in loopcnt:
    for j in range(item):
        print("%s " %result[cnt], end='')
        cnt+=1
    print()
