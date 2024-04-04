a = 60
b = 13
# a b & 연산하면 001100임, 001100 10진수 변환하면 12
if a & b == 12:
    print(1)
else:
    print(2)

c = 100
result = 0
for i in range(1, 5):
    result *= c >> 2
    result = result + 1
    print(result)

