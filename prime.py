def prime_number(N):
    i = 2
    flag = True
    while i*i <= N:
        if N % i == 0:
            flag = False
            break
        i+=1
    if flag:
        return "PRIME NUMBER"
    return "NOT PRIME NUMBER"

if __name__=='__main__':
    N = 100
    for i in range(1,N+1):
        print(f"{i} is {prime_number(i)}")
