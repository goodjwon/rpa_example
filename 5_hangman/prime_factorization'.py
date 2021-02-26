# 약수 구하니?
# 약수란?? 나누는 수?
# 어떻게 구해??
# 나누어서 나머지가 0인 수..

# 1. 숫자입력 ok
# 2. 계속 나누어 나머지가 0인지 확인
# 3. 나누는 수는 계속 증가
# 4. 입력한 수와 같을때 까지
# https://oceancoding.blogspot.com/2019/10/blog-post.html

import time

cnt = int(input('약수를 구할 횟수 입력:'))

divs = []

for i in range(cnt):
    n = int(input('숫자 입력:'))

    d = []
    s = time.time()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)

    divs.append(set(d))
    print(n, '의 약수 : ', *d, '\n소요시간 : ', time.time() - s, '(sec)')
    print()

if cnt > 1:
    comdiv = set.intersection(*divs)
    print('공약수 : ', *comdiv)
    print('최대 공약수 : ', max(comdiv))