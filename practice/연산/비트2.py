a = 100
r = 0

# 10진수 > 2진수 : bin()
ato2 = (bin(a)[2:])

em = list()
for i in str(ato2):
    em.append(i)
print(em)

em = list(map(int, em))
print(em)

str1 = ''.join(map(str, em))
print(str1)

# 리스트 뒤집기
em.reverse()

# 문자열 리스트를 정수로 변환
mm = list(map(int, em))
print(mm)

# 리스트 원소를 숫자로
str2 = ''.join(map(str, mm))
print(str2)

toInt1 = int(str1)
toInt2 = int(str2)

#  ^ 연산은 두 비트가 서로 다를 때 결과 1
# 여기서, 두 비트는 다르므로 1이 실행되고, if문이 실행
# == 0을 붙여보 면, else로 넘어가게됨
if toInt1 ^ toInt2 == 0:
    res = toInt2 ^ toInt2
    print(res)
else:
    print("False")
