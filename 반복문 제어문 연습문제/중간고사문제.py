cnt = 1

while True:
    if cnt!=1 and cnt%5==1:
        if input("계속하시겠습니까? Y/N : ").upper() == "N":
            print("게임을 종료합니다.")
            break
        
    if cnt%2:
        temp = input("입력 : ")
        if cnt%3==0:
            if temp != "짝":
                print("졌습니다!")
                break
        else:
            if temp == "짝" or int(temp) != cnt:
                print("졌습니다!")
                break
    else:
        if cnt%3==0:
            print("상대 : 짝")
        else:
            print("상대 : %d" %cnt)
    cnt += 1
