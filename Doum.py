## 문자열 Level 1.함수 사용해보기
"""
str = "Hello, world"

# 'l'이 몇번 들어갔는지 출력
print(str.count("l"))

# 'o'의 인덱스 값 출력
print(str.index("o"))

# 'abcd'를 'a, b, c, d'로 만들고 출력
print(", ".join('abcd'))

# 'world'를 'python'으로 바꾸기
print(str.replace("world", "python"))

# str을 ' '로 구분자로 하여 나누고 출력
print(str.split())
"""

## 리스트 Level 1.함수 사용해보기
"""
list = [1, 7, 5, 4]

# 6 추가
list.append(6)
print(list)

# 오름차순 정렬
list.sort()
print(list)

# 역순으로 뒤집기
list.reverse()
print(list)

# 4 인덱스 값 출력
print(list.index(4))

# 4 삭제 후 출력
list.remove(4)
print(list)

# 맨 처음에 10 추가 후 출력
list.insert(0, 10)
print(list)
"""

## 딕셔너리 Level 1. 함수 사용해보기
"""
dic = {'name' : 'kim', 'phone' : '010-9999-1234', 'brith' : '0329'}

# value값 모두 출력
print(dic.values())

# key가 name인 value를 출력
print(dic.get('name'))

# key값 모두 출력
print(dic.keys())

# key와 value를 묶어서 요소들을 모두 출력
print(dic.items())

# 모든 요소 삭제 후 dic 출력
dic.clear()
print(dic)

# birth가 있는지 출력
print('birth'in(dic))
"""

## 집합 Level 1. 함수 사용해보기
"""
# set1에 4를 추가한 후 출력
set1 = set([1, 2, 3])

set1.add(4)
print(set1)

# set1에 5, 6을 한꺼번에 추가한 후 출력
set1.update([5, 6])
print(set1)

# set1에서 3 삭제 후 출력
set1.remove(3)
print(set1)
"""

## 문자열 Level 2. 문자열 슬라이싱
"""
T = int(input())

i = 0
while i < T :
    str1 = str(input())
    i += 1

    print(str1[0]+ str1[-1])
"""

## 리스트 Level 2. split
"""
#킹(1) 퀸(1) 룩(2) 비숍(2) 나이트(2) 폰(8)
K, Q, R, B, N, P = map(int, input().split())

chess = [K, Q, R, B ,N, P]

print(1 - chess[0], 1 - chess[1], 2 - chess[2], 2 - chess[3], 2 - chess[4], 8 - chess[5])
"""

## 딕셔너리 Level 2. 딕셔너리 응용
"""
"""

## 집합 Level 2. 집합과 문자열
"""
"""

## 문자열 Level 3. 이스케이프 문자
"""
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")
"""

## 리스트 Level 3. min max
"""
bur = []
bev = []

bur.append(int(input())) #상덕버거
bur.append(int(input())) #중덕버거
bur.append(int(input())) #하덕버거

bev.append(int(input())) #콜라
bev.append(int(input())) #사이다

print(min(bur) + min(bev) -50)
"""

## 딕셔너리 Level 3. 딕셔너리와 문자열
# 지아 누나 코드
"""
dic = {}
list = []

n = int(input())

for i in range(n):
    book = input()
    if book not in dic:
        dic[book] = 1
    else:
        dic[book] += 1

num = max(dic.values())

for i in dic:
    if num == dic[i]:
        list.append(i)

list.sort()
print(list[0])
"""
