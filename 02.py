a = list(range(0, 10, 3))
print(a)

for b in a :
    print(b)

# for문과 range 함수를 사용해서 0~99까지 수를 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성
result = []
c = list(range(0, 100))
for d in c :
    result.append(d)
print(result)

# i = 2065743
# count = 0
# while i < 384657029:
#     i = i + 1
#     count = count + 1
#     print("i는 지금 값이", i, "이므로, 100보다 작습니다.")
# print(count)

# while문을 사용하여 대기번호를 출력하는 프로그램을 작성
# 최대 대기번호 발행수는 1000
i = 0
while i < 1000 :
    i = i + 1
    # if i == 500 :
    #     break
    print("대기번호", i, "번")
else:
    print("대기번호가 1000번 초과입니다.")

# while문을 사용하여 1부터 100까지 수
index = 0
result = 0
while index < 100 :
    index = index + 1
# 그 존재하는 모든 홀수
    if index % 2 == 1:

# 홀수라면 그 값을 저장
        result = result + index
# 의 합을 구하시오.
print(result)

x = []
i = 0
while i < 100:
    i = i + 1
    if i % 2 == 1:
        x.append(i)
print(sum(x))

# 다음 리스트 변수의 평균 값을 구하여라.
# 평균값을 구할 때는 for 반복문을 사용.
my_list = [100, 200, 400, 800, 1000, 1300]
result = 0
for i in my_list:
    result = result + i
avg = result / len(my_list)
print(int(avg))

# while문을 사용하여 1부터 45사이의
import random
i = 0
r = []
while i < 6:
    i = i + 1
    p = random.randint(1, 45)
    r.append(p)
print(r)

# 랜덤한 수 6개를 생성하고,
# 이를 result 리스트 변수에 추가하는 코드를 작성

import random
random.randint(1, 45)

