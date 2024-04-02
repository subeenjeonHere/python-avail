# 파이썬 비트 연산자
a = 100
b = 100
result = 0
result2 = 0
for i in range(1, 3):
    result = a >> i
    result = result + 1
    result2 = a << i
print(result)
print(result2)
