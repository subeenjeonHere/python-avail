class charClass:
    a = ["Seoul", "Inchon", "Daejun"]

myVal = charClass()
str01 = ''

# charClass의 a 리스트 범위까지 반복
# a 리스트를 i에 순서대로 대입
for i in myVal.a:
    # str01에 i의 0번째 문자를 더함
    str01 = str01 + i[0]
print(str01)
