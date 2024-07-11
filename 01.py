dic = {"봄": "숭어", "여름": "덥죠", "숫자": 3}

for var in dic :
    print(var, dic[var])

string = "오늘은 너무 덥네요. 빨리 집에 가고 싶어요."
for s in string :
    print(s)

# 리스트 변수는 네 개의 정수가 저장되어 있다.
# for문을 사용해서 리스트 변수의 요소 중 음수를 화면에 출력하시오.
numbers = [3, -20, -3, 44]
for num in numbers :
    if num < 0 :
        print(num)