def prime_number(N):
    if N==1: return "NOT PRIME NUMBER" # 이 방법밖에 없네요;;
    i = 2
    flag = False # 기본값을 False로 설정 > N=1일 때 NOT PRIME으로 판단하도록
    while i*i <= N:
        if N % i == 0:
            flag = False
            break
        i+=1
    else: # python 문법: for,while 반복문이 중간에 'break'에 의해 끊기지 않고 정상적으로 순환을 완료했을 때 코드 흐름은 else 절로 진입한다.
        flag = True # sqrt(N)보다 작은 모든 제곱수로 나누었을 때 나누어 떨어지지 않는다면 N은 소수.
    if flag:
        return "PRIME NUMBER"
    return "NOT PRIME NUMBER"

if __name__=='__main__':
    N = 100
    for i in range(1,N+1):
        print(f"{i} is {prime_number(i)}")
