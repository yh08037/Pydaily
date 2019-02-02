# def check_id(message):
#     for i in message:
#         if i != 0 or  i != 1 or i != 2 or i != 3 or i != 4 or i !=5 or i != 6 or i != 7 or i != 8 or i != 9:
#             print("아이디는 문자와 숫자가 같이 포함되어야 합니다")

def check_id(message):
	return not(message.isalpha() or message.isdigit())


def generate_password():
    import random
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a = random.choice(alp)
    b = random.choice(alp)
    c = random.choice(alp)
    d = random.choice(alp)
    e = random.choice(alp)
    f = random.choice(alp)
    return (a+b+c+d+e+f)


def input_addinfo(info1, info2):
    return [info1, info2]


def display_member(member):
    for j in range(2):
        weight_a = d[j][1]
        height_a = d[j][2]
        print("아이디 : ", d[j][0])
        print("비밀번호 : ", generate_password())
        print("추가정보 : ", input_addinfo(weight_a, height_a))


d = []

for i in range(2):
    lst = []
    while True:
        user_id = input("아이디 입력 : ")
        if check_id(user_id):
            break
        else:
            print("아이디는 문자와 숫자가 같이 포함되어야 합니다")
    lst.append(user_id)
    height = int(input("신장 입력 : "))
    lst.append(height)
    weight = float(input("몸무게 입력 : "))
    lst.append(weight)
    d.append(lst)

display_member(d)
