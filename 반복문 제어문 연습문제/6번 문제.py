# m, n의 최대공약수, 최소공배수 찾기

def gcd(m, n):
    if m > n :
        m, n = n, m
        
    # m <= n
    
    for i in range(m, 0, -1):
        if n % i == 0 and m % i == 0: # 중요!
            return i


def lcm(m, n):
    if m > n :
        m, n = n, m
        
    # m <= n
    
    i = n
    while True:
        if i % n == 0 and i % m == 0:
            return i
        i += 1


a = int(input("A : "))
b = int(input("B : "))

print("최대공약수 : %d" %gcd(a, b))
print("최소공배수 : %d" %lcm(a, b))
    