# 사용자가 입력한 수가 3의 배수이면 ok를 출력하는 프로그램을 작성하시오.
# 그렇지 않으면 no를 출력하시오.

num = int(input("임의의 수를 입력하세요: "))

if num % 3 == 0 :
    print("ok")
else :
    print("no")

var = [1,2,3]
if 3 in var :
    print("원하는 숫자가 있습니다.")
else :
    print("찾으시는 숫자가 없습니다.")

fruits = ['사과', '바나나', '딸기']

for var in fruits :
    print("이것은 첫번째 코드블록 라인입니다. ", var)
    print("이것은 두번째 코드블록 라인입니다. ", var)
print("이는 for 반복문의 코드블록 밖입니다.")

# 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for문을 사용해서 화면에 출력
# 단 부가세는 10%로 가정
numbers = [100,200,300]
for num in numbers :
    print(num + (num * 0.1))