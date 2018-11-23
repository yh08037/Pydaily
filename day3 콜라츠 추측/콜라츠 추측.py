def collatz(num):
    cnt = 1
    while True:
        if cnt == 500 :
            cnt = -1
            break
        elif num % 2 == 0 :
            num /= 2
            if num == 1:
                break
        else:
            num = num*3+1
        cnt += 1

    return cnt

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(626331))